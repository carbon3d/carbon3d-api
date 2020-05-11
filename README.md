# Carbon API
Welcome to the Carbon DLS API. 
The documentation here will help you get started integrating with our API, but first, **make sure you've reached out to your Carbon Technical Partner and signed all the required documents**.

## Getting Started
We are excited for you to start using Carbon's API, but there are a few things you should keep in mind as you start integrating with us.
1. Our API is still in Early Access, so please be patient as we add more functionality. Feel free to share your feedback.
2. We have prioritized developing functionality for mass customized parts of similar geometry. At this time, we cannot guarantee that utilizing our order / packing system will work for other applications.
3. Currently, we are only providing examples in python but our REST API itself is language agnostic. 

The documentation in this wiki is intended to help you get started and provide some examples, but detailed documentation about each request can be found at [https://api.carbon3d.com/v1/api-docs/#/](https://api.carbon3d.com/v1/api-docs/#/). 

### Authentication
The Carbon API uses a [JWT](https://en.wikipedia.org/wiki/JSON_Web_Token) token to authenticate each request. Follow these steps to get started.
1. Generate an API Key [here](https://carbon3d.print.carbon3d.com/api_keys)* by clicking the "Create API Key" button. This will automatically download a `secrets.json` file; your client secret is NOT stored by Carbon.
2. You can now use the `authenticate-create.py`script to generate a valid token with your desired expiration. You can re-generate as many tokens as you'd like with new expirations utilizing the same secret.
`# generate an access token that is valid for 24 hours
v1/python/examples/authtoken-create.py path/to/secret.json --exp_hours 24`
3. You must now add an HTTP header `Authorization: Bearer [token]` in all of your requests.

*If you can't access this page, please reach out to your Carbon Technical Partner to discuss gaining access to our Early Access Program.

### Definitions
**Models:** A 3d file representing a geometry with no particular orientation, supports, etc. Models can belong to multiple parts.
**Parts:** A printable model design which has a specific orientation, resin, etc.
**Printed Parts:** A specific instance of a part that has been printed and properly serialized.
**Orders:** A logical grouping of parts you would like to print on as few builds as possible.
**Builds:** A printable set of parts arranged on a build platform ready for printing.  
## Examples
### Python
Read more about our Python examples [here](v1/python_examples/README.md)

## Frequently Asked Questions
### What is an application id?
You can think of an Application as a shareable folder for models, parts, projects, etc. that are related to each other. For many of you, Carbon printers are only ever used for printing a single type of part (e.g. models) and none of that information ever needs to be shared. For others however, you might want to have one Application for the car seat cushion you are working on and another for face shields. Functionality to share and manage your applications hasn't been exposed yet, so if you think you want to change how your applications are set up please reach out to your Carbon Technical Partner.

### What's the difference between a model and a part?
Models can't be printed, they just represent 3d dimensional shapes that can be used in a variety of parts. For example, you could have a model for an iPhone case that is used in 2 parts, one that is printed in EPU 41 and another in UMA 90.

### What's the difference between a project and a build?
A project is a collection of builds that have been modified over time. For example, lets say you open our project editing software, upload 10 models, then click print. Afterwards, you realize you want to change the orientation of a few of the models so you open the project again, modify the orientation, and click print. You printed the same project but two different builds.

### How can I queue a build?
We haven't exposed this endpoint yet, look out for updates.

### Why can't I see my models, orders, etc. in the UI.
Please let us know if you'd like to see these concepts exposed in our UI.

### What is a part number?
Part numbers are a common term used in manufacturing to denote a reference to a particular _part design_. Each company chooses their own conventions for assigning part numbers, but generally a single part number is capable of having multiple versions or revisions. It is important to understand that a part number identifies a part _design_ as opposed to serial numbers which are unique identifiers for _a particular instantiation_ of that part design.

### Are there any API calls that allow me to interact with the printer (e.g. start a print, open the door, etc)?
Unfortunately, this API is not intended to facilitate robotic automation for a printer. If this is something you need, please let your Carbon Technical Partner know.


### Can you add ____ to the print data we are able to export?
Please submit the request via <api-list@carbon3d.com>

## Feedback
Please send all questions and feedback to <api-list@carbon3d.com>

