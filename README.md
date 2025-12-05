LiveClass (Model) → live_at
Cron Job running every minute which will pick all the classes getting live exactly after 15 mins from now.
	
Celery
PubSub 
Message Broker
Publisher
Worker

Task 1 → Figure out all the classes starting in 15 mins.
Task 2 → Will be triggered by Task 1 ( many triggers ) ( Now we can ensure in-time execution of Task 2 )

UserEnrollment (Model) User ←→ LiveClass
Now when we find a class getting live we can find all the enrolled users and submit the notification payload for all these users.


LLD for Notification Service
CRUD APIs to manage events and templates.
Worker configured.

Logic Flow for the worker

Loop and check for the payloads in the queue.

If a payload is found then it will pick the payload.

It will also make the message invisible in the queue.

It will also add a lock in redis for it to not pick any other message or even a lock for payload.

It will verify if the given Event, template and users exist in the system. Delete and raise exceptions on logging tools if not found.

If payload is valid it will trigger notification using clients in the service. ( example message91 client )

If this is successful it will delete the payload.

If failed we will decide if event is real time.
If yes —> Delete it.
If no —> Put it in DLQ
After the execution cycle is complete all the redis locks are released.

And the worker will end up at the start of the loop.


