### Pulling instagram biography and other data


In the environment file `.env` set the `COOKIE` to your instagram cookie, and the `USER_FILE` to the file with user ids.

User file should look like this:
```text
1111111
2222222
3333333
4444444
```

#### Running the script

Create a virtual env and install the requirements
```shell script
$ python -m venv venv
# Linux activation
$ source venv/bin/activate
# Windows activation
$ venv/Scripts/activate.bat
# And install requirements
$ pip install -r requirements.txt
```

and just run
`$ python main.py`

If you want to add another param to the json, just change in `main.py` this:

```python
if __name__ == '__main__':
    run_bot(settings.URL, users, settings.HEADERS, 'is_private', 'is_interest_account')
```
Other example data that can be pulled:
```text
pk
username
full_name
is_private
profile_pic_url
profile_pic_id
is_verified
has_anonymous_profile_picture
media_count
follower_count
following_count
following_tag_count
biography
external_url
external_lynx_url
total_igtv_videos
has_igtv_series
total_clips_count
total_ar_effects
usertags_count
is_favorite
is_interest_account
hd_profile_pic_versions
hd_profile_pic_url_info
mutual_followers_count
show_shoppable_feed
shoppable_posts_count
can_be_reported_as_fraud
merchant_checkout_style
seller_shoppable_feed_type
has_highlight_reels
has_guides
is_eligible_for_smb_support_flow
displayed_action_button_partner
smb_delivery_partner
smb_support_partner
smb_donation_partner
smb_support_delivery_partner
displayed_action_button_type
direct_messaging
address_street
business_contact_method
category
city_id
city_name
contact_phone_number
is_call_to_action_enabled
latitude
longitude
public_email
public_phone_country_code
public_phone_number
zip
instagram_location_id
is_business
account_type
professional_conversion_suggested_account_type
can_hide_category
can_hide_public_contacts
should_show_category
should_show_public_contacts
account_badges
whatsapp_number
include_direct_blacklist_status
is_potential_business
show_post_insights_entry_point
is_bestie
has_unseen_besties_media
show_account_transparency_details
auto_expand_chaining
highlight_reshare_disabled
is_memorialized
open_external_url_with_in_app_browser
```
