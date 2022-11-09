# Steps to follow

1. Open Google Cloud Shell

	In your home directory create a virtual environment using the command below

	python3 -m venv myenv

2. Activate the environment:

	source myenv/bin/activate

3. You can download the files in this repository using the download button given above. 
In the home directory make a folder called 'dash-gcp-template' and drop the files extracted from the downlaoded zip file into 'dash-gcp-template'
Alternative; You can also clone your repository using git using the command from the home directory

`git clone https://gitlab.com/mobibootcamp/dash-gcp-template.git`

This will create a directory 'dash-gcp-template' and will download all the files from the git repository

4. Cd to home directory and run the below command

	pip install -r ./dash-gcp-template/requirements.txt

5. After all the packages are downloaded, cd to 'dash-gcp-template' folder start the app using the command below:

	python3 main.py

After the above step, you can see your app running at port 8080 by clicking on Web Preview icon on the cloud console.

6. To deploy to GCP, select the project to which you want to deploy through the dropdown box in the Google cloud console terminal and then run the below command:

	gcloud app deploy

Once deployed your project URL is displayed which you can invoke to see your application on GCP. You can now send this link to anyone who wishes to see your project

The above steps are high level. You may have to follow the GCP prompts for login, enabling certain API permissions for the project etc..

# Selenimum references
* https://selenium-python.readthedocs.io/installation.html
* https://selenium-python.readthedocs.io/waits.html - refer how to wait for the element to load
