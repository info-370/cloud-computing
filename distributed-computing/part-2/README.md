# Instructions

## Setting up Elastic Beanstalk

### Initial Setup
* In the aws console, select `Elastic Beanstalk` under the `Compute` heading.
* Click `Create New Application`

### Application Info
* Choose an application name
    * _note_: This must be unique. Name it something like `info370-<your_netid>-lab6`
* Select `Create web server`

### Environment Type
* **Predefined configuration:** Python
* **Environment type:** Load balancing, auto scaling
* Upload your zip (I have already created a zip for you in `application.zip`)
* Leave the `deployment preferences` section as the defaults
* Leave Environment name and Environment URL as the default
* Under `Additional Resources` leave both boxes **unchecked**

### Configuration Details
* **Instance Type**: t1.micro
* **EC2 Keypair**: You can leave this blank
* **Application heal check URL**: /
* Everything else can be left as its default or blank

### Environment Tags
Leave this section blank

### Permissions
Leave this section with defaults

### Notes
* Once you launch your instance, it can take 5-10 minutes for your environment to be ready. While you wait, I suggest you talk with your final project group or help those around you so you don't have to spend too much time sitting around.
* After your environment has been created, you will need to set it so that there are more instances (3-4 should be fine). To do this, go to your environment dashboard and select the configuration tab from the side menu
   * You should see a box with settings that says `Scaling`. Click the gear and set minimum instances to 3 and the maximum to 3. We are doing this to maximize the speed benefit of using a cluster (usually elastic beanstalk won't scale up until it reaches thousands of requests).

## Testing
To test your solution, I have written a small script in `test.py`. In this file you will need to change the global variable `url` to whatever the url of your elastic beanstalk cluster is (the url can be found at the top of your elastic beanstalk dashboard for that environment. Make sure you include the protocol piece of the url: `https://`).

When you are done, feel free to talk with your final project group.
