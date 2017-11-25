# PROD
Project at CTC11 - Persuasive Release of Open Data - building a case for the release of Open Data in Aberdeen. Exporing possibilities to automate requests to get the data, if we can't get a portal.

We will use the what do they know API to automate the requests: https://www.whatdotheyknow.com/help/api

Some helpful hints here: https://www.mysociety.org/2016/12/19/alaveteli-for-campaigners-how-to-create-pre-written-requests-for-your-supporters/?refferer=mailnotify&uid=138 

I have adapted this below. 

It’s quite simple to create these yourself. Just build the URL up in steps:

The base URL https://www.whatdotheyknow.com/

Begin by telling the site that this is a new request: https://www.whatdotheyknow.com/new/

Add a forward slash (/) and then the body you want the request to be sent to (exactly as it is written in the url of the body’s page of the website): https://www.whatdotheyknow.com/new/aberdeen_city_council

Add a question mark: This tells the website that we are going to introduce a ‘parameter string’. Now our URL looks like this: https://www.whatdotheyknow.com/new/aberdeen_city_council?

Input a title: we need to indicate that the next part should go into the ‘title’ field, like this: 
https://www.whatdotheyknow.com/new/aberdeen_city_council?title= 
and then dictate what the title should be: 
https://www.whatdotheyknow.com/new/aberdeen_city_council?title=EV%20Charging%20Points

Notice that if there is a space between words, it should be shown as %20. To make the process of encoding the URLs easier, you can use an encoder tool like this one: https://meyerweb.com/eric/tools/dencoder/

Input the body of the request, again using ‘%20’ between each word. This is where your URL can become very long! We use the parameter default_letter 

The salutation (Dear…) and signoff (Yours…) are automatically wrapped around this by the site, so there’s no need to include them:

https://www.whatdotheyknow.com/new/aberdeen_city_council?title=EV%20Charging%20Points&default_letter=

Then add the text of the request. In our example, "geo-located list of charging points for electrical vehicles" becomes this when encoded: 

a%20geo-located%20list%20of%20charging%20points%20for%20electrical%20vehicles%2C%20along%20with%20a%20note%20of%20the%20frequency%20of%20the%20update%20of%20this%20data%20set%20(e.g.%20Monthly%2C%20Quarterly%2C%20Annually)

So, stringing these together we get:
https://www.whatdotheyknow.com/new/aberdeen_city_council?title=EV%20Charging%20Points&default_letter=a%20geo-located%20list%20of%20charging%20points%20for%20electrical%20vehicles%2C%20along%20with%20a%20note%20of%20the%20frequency%20of%20the%20update%20of%20this%20data%20set%20(e.g.%20Monthly%2C%20Quarterly%2C%20Annually)


Finally we can use tags. This allows you to add a space-separated list of tags, so for example you can identify any requests made through your campaign or which refer to the same topic. 

So, we can add "&tags=ODIAberden%20CTC11" which will tag the request ODIAberdeen and CTC11.

The final URL we end up with is:

https://www.whatdotheyknow.com/new/aberdeen_city_council?title=EV%20Charging%20Points&default_letter=a%20geo-located%20list%20of%20charging%20points%20for%20electrical%20vehicles%2C%20along%20with%20a%20note%20of%20the%20frequency%20of%20the%20update%20of%20this%20data%20set%20(e.g.%20Monthly%2C%20Quarterly%2C%20Annually)&tags=ODIAberden%20CTC11

