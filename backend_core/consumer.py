import pika, json, os
from core import Degree, db, User

# Get RabbitMQ URL from environment variable
rabbitmq_url = os.environ.get('RABBITMQ_URL')
if not rabbitmq_url:
    raise ValueError("RABBITMQ_URL environment variable not set")

params = pika.URLParameters(rabbitmq_url)

# Create a connection
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='core')

# Defining a callback function
def callback(ch, method, properties, body):
    print('Received in config')
    data = json.loads(body)
    print(data)
    
    model_type = data.get('model')
    instance_id = data.get('id')
    action = data.get('action')
    user_id = data.get('user_id', None)  # Include user_id if provided

    if model_type == 'school':
        handle_school(instance_id, action)
    elif model_type == 'degree':
        handle_degree(instance_id, action, user_id)
    elif model_type == 'degreeview':
        handle_degreeview(instance_id, action)
    elif model_type == 'userprofile':
        handle_userprofile(instance_id, action)
    else:
        print(f"Unknown model type: {model_type}")

def handle_school(instance_id, action):
    try:
        school = School.objects.get(id=instance_id)
        if action == 'update_logo':
            new_logo = action.get('new_logo')
            if new_logo:
                school.logo = new_logo
                school.save()
                print(f"Logo updated for school {instance_id}")
            else:
                print("New logo URL not provided.")
        elif action == 'update_description':
            new_description = action.get('new_description')
            if new_description:
                school.description = new_description
                school.save()
                print(f"Description updated for school {instance_id}")
            else:
                print("New description not provided.")
        else:
            print(f"Unknown action: {action} for school")
    except School.DoesNotExist:
        print(f"School with id {instance_id} does not exist.")

def handle_degree(instance_id, action, user_id=None):
    try:
        degree = Degree.objects.get(id=instance_id)
        if action == 'increase_view_count':
            degree.view_count += 1
            degree.save()
            print('Degree view count increased!')
        elif action == 'add_like':
            if user_id:
                user = User.objects.get(id=user_id)
                degree.likes.add(user)
                degree.save()
                print(f'User {user_id} liked degree {instance_id}')
            else:
                print('User ID is required for adding like.')
        elif action == 'add_save':
            if user_id:
                user = User.objects.get(id=user_id)
                degree.save.add(user)
                degree.save()
                print(f'User {user_id} saved degree {instance_id}')
            else:
                print('User ID is required for saving degree.')
        else:
            print(f"Unknown action: {action}")
    except Degree.DoesNotExist:
        print(f"Degree with id {instance_id} does not exist.")
    except User.DoesNotExist:
        print(f"User with id {user_id} does not exist.")

def handle_degreeview(instance_id, action):
    try:
        degree_view = DegreeView.objects.get(id=instance_id)
        if action == 'log_view':
            # This action could log the view or perform some analysis
            print(f"Degree view logged for degree view {instance_id}")
        else:
            print(f"Unknown action: {action} for degree view")
    except DegreeView.DoesNotExist:
        print(f"DegreeView with id {instance_id} does not exist.")

def handle_userprofile(instance_id, action):
    try:
        user_profile = UserProfile.objects.get(id=instance_id)
        if action == 'update_profile_picture':
            # This action would update the profile picture
            new_picture = action.get('new_picture')
            if new_picture:
                user_profile.profile_picture = new_picture
                user_profile.save()
                print(f"Profile picture updated for user profile {instance_id}")
            else:
                print("New profile picture URL not provided.")
        elif action == 'update_bio':
            # This action would update the bio
            new_bio = action.get('new_bio')
            if new_bio:
                user_profile.bio = new_bio
                user_profile.save()
                print(f"Bio updated for user profile {instance_id}")
            else:
                print("New bio not provided.")
        else:
            print(f"Unknown action: {action} for user profile")
    except UserProfile.DoesNotExist:
        print(f"UserProfile with id {instance_id} does not exist.")

# Initiating message consumption
channel.basic_consume(queue='config', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()
