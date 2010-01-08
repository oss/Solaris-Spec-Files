Summary:	SquirrelMail webmail client (Rutgers customized)
Name:		squirrelmail
Version:	1.4.16
Release: 	13
License:	GPL
Group:		Applications/Internet
Source:		%{name}-%{version}.tar.bz2
Source1: 	webmail-webtools.tar
Source2: 	abook_group-0.51.1-1.4.2.tar.gz
Source3: 	abook_import_export-1.1-1.4.4.tar.gz
Source4: 	addgraphics-2.3-1.0.3.tar.gz
Source5: 	add_address-1.0-1.4.0.tar.gz
Source6: 	archive_mail.1.2-1.4.2.tar.gz
Source7: 	auto_cc-2.0-1.2.tar.gz
Source8: 	autocomplete.2.0-1.0.0.tar.gz
Source9: 	bounce-0.5-1.4.x.tar.gz
Source10: 	compatibility-2.0.13-1.0.tar.gz
Source11: 	compose_chars-0.1-1.4.tar.gz
Source12: 	dictionary-0.6.tar.gz
Source13: 	folder_settings-0.3-1.4.0.tar.gz
Source14: 	folder_sizes-1.5-1.4.0.tar.gz
Source15: 	folder_synch.0.8-1.4.0.tar.gz
Source16: 	jump_to_folder.0.3-1.2.7.tar.gz
Source17: 	legend.1.2-1.2.8.tar.gz
Source18: 	limit_languages-1.0-1.4.0.tar.gz
Source19: 	login_notes-1.2-1.4.0.tar.gz
Source20: 	mark_read-1.4.2-1.2.tar.gz
Source21: 	notify_1_3.tar.gz
Source22: 	pupdate.0.7-1.4.2.tar.gz
Source23: 	quicksave-2.4.2-1.2.9.tar.gz
Source24: 	select_range-3.5.tar.gz
Source26: 	show_headers-1.3-1.4.tar.gz
Source27: 	startup_folder-2.1-1.4.0.tar.gz
Source28: 	timeout_user-1.1.1-0.5.tar.gz
Source29: 	twc_weather-1.3p3b-RC2.tar.gz
Source30: 	user_special_mailboxes.0.1-1.4.tar.gz
Source31: 	variable_sent_folder.0.4-1.4.tar.gz
Source32: 	view_as_html-3.6-1.4.x.tar.gz
Source33: 	autosubscribe-1.1-1.4.2.tar.gz 
Source34: 	spam_buttons-1.0-1.4.tar.gz
Source35: 	restrict_senders-1.5beta3-1.4.1.tar.gz
Source36: 	lockout-1.6-1.4.1.tar.gz
Source37: 	preview_pane-1.2-1.4.3.tar.gz
Source39:	image_buttons-1.4-1.4.tar.gz
Source40:	msg_flags-1.4.15a-1.4.3.tar.gz
Source41:	squirrel_logger-2.3beta2-1.2.7.tar.gz
Source42:	verify_reply_to-1.0-2.8.tar.gz
Source43:	forced_prefs-1.4.sm-1.4.0.tar.gz
Source44:	generic_info.tar.gz
Source45:	empty_folders-2.0-1.2.tar.gz
Source46:	login_activity-1.0-1.4.0.tar.gz
Source47:	rulogin.tar
Patch2:		mbstring_disabled.patch
Patch3:		logindisabled.patch
Patch4:		plugin_login_notes.patch
Patch5:		plugin_select_range.patch
Patch7:		plugin_dictionary.patch
Patch8:		ldapfix.patch
Patch9: 	autocomplete.diff
Patch10: 	plugin_spam_buttons.patch
Patch11:	plugin_twc_weather.patch
Patch12:	boldoptions.patch	
Patch13:	plugin_image_buttons.patch
Patch16:	plugin_timeout_user.patch
Patch17:	plugin_verify_reply_to.patch
Patch18:	long_folder_names.patch
Patch19:	favicon.patch
Patch20: 	plugin_image_buttons_white_fix.patch
URL: 		http://www.squirrelmail.org/
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root
Requires:       perl
Requires:       ispell
Requires:       webtools
Requires:       pear-Validate
Requires:       check-criteria


%define sqmaildir /usr/local/squirrelmail-%{version}

%description
SquirrelMail is a standards-based Webmail package written in PHP4.
It includes built-in pure PHP support for the IMAP and SMTP protocols,
and all pages are rendered in pure HTML 4.0 for maximum compatibility
across browsers. It has very few requirements, and is very easy to
configure and install. It has all the functionality you would want
from an email client, including strong MIME support, address books,
and folder manipulation.

%package plugins
Summary:	SquirrelMail plugins
Group:		Applications/Internet
Requires:	%{name} = %{version}-%{release}

%description plugins
abook_group-0.51.1-1.4.2       		- Address Group Plugin
abook_import_export-1.1-1.4.4  		- Addressbook Import-Export
addgraphics-2.3-1.0.3          		- Add Graphics
add_address-1.0-1.4.0          		- Add address
archive_mail-1.2-1.4.2         		- Archive Mail
auto_cc-2.0-1.2                		- Auto CC
autocomplete.2.0-1.0.0         		- Autocomplete
autosubscribe-1.1-1.4.2        		- Autosubscribe
bounce-0.5-1.4.x               		- Bounce
compatibility-2.0.13-1.0       		- Compatibility
compose_chars-0.1-1.4          		- Compose Special Characters
dictionary-0.6                 		- Dictionary
empty_folders-2.0-1.2			- Empty Folders
folder_settings-0.3-1.4.0      		- Folder Settings
folder_sizes-1.5-1.4.0         		- Folder Sizes
folder_synch.0.8-1.4.0         		- Folder Synch
forced_prefs-1.4.sm-1.4.0		- Forced Preferences
jump_to_folder.0.3-1.2.7       		- Jump to Folder
legend.1.2-1.2.8               		- Highlighting Legend
limit_languages-1.0-1.4.0      		- Limit Languages
lockout-1.6-1.4.1              		- Lockout
login_activity-1.0-1.4.0		- Login Activity
login_notes-1.2-1.4.0          		- Login Notes
mark_read-1.4.2-1.2            		- Mark Read
msg_flags-1.4.15a-1.4.3	       		- Message Flags
notify_1_3                     		- Notify New Mail Popup
preview_pane-1.2-1.4.3         		- Preview Pane
pupdate.0.7-1.4.2              		- Plugin Updates
quicksave-2.4.2-1.2.9          		- Quick Save
select_range-3.5               		- Select Range
restrict_senders-1.5beta3-1.4.1     	- Restricted Senders
show_headers-1.3-1.4           		- Show Headers
spam_buttons-1.0-1.4           		- Spam Buttons
squirrel_logger-2.3beta2-1.2.7      		- Squirrel Logger
startup_folder-2.1-1.4.0       		- Startup Folder
timeout_user-1.1.1-0.5         		- Timeout User
twc_weather-1.3p3b-RC2         		- TWC Weather
user_special_mailboxes.0.1-1.4 		- User Special Mailboxes
variable_sent_folder.0.4-1.4   		- Variable Sent Folder
verify_reply_to-1.0-2.8	       		- Verify Reply-To
view_as_html-3.6-1.4.x         		- View as HTML

%package webtools-plugins
Summary:	SquirrelMail webtools plugins
Group:		Applications/Internet
Requires:       %{name} = %{version}-%{release}

%description webtools-plugins
webtools

%package ru-plugins
Summary:	SquirrelMail webtools plugins
Group:		Applications/Internet
Requires:       %{name} = %{version}-%{release}

%description ru-plugins
Rutgers home-grown Squirrelmail Plugins

image_buttons-1.4-1.4
generic_info-1.0 

%package geoip
Summary:	SquirrelMail for php5 
Group:		Applications/Internet
Requires:	%{name} = %{version}-%{release}
Requires:       mod_geoip

%description geoip 
This package provides dependant geoip packages for squirrelmail.

SquirrelMail is a standards-based Webmail package written in PHP4.
It includes built-in pure PHP support for the IMAP and SMTP protocols,
and all pages are rendered in pure HTML 4.0 for maximum compatibility
across browsers. It has very few requirements, and is very easy to
configure and install. It has all the functionality you would want
from an email client, including strong MIME support, address books,
and folder manipulation.


%prep
PATH="/usr/local/gnu/bin:/usr/local/bin:/usr/sfw/bin:$PATH"
export PATH

%setup -q
##REMOVES NASTY ~ FILES
%__patch --no-backup-if-mismatch -p1 < %PATCH2
%__patch --no-backup-if-mismatch -p1 < %PATCH3
%__patch --no-backup-if-mismatch -p1 < %PATCH8
cd src
%__patch --no-backup-if-mismatch -p0 < %PATCH12
%__patch --no-backup-if-mismatch -p1 < %PATCH19

cd ..

cd plugins
tar -xf %{_sourcedir}/webmail-webtools.tar
gzip -dc %{_sourcedir}/abook_group-0.51.1-1.4.2.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/abook_import_export-1.1-1.4.4.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/addgraphics-2.3-1.0.3.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/add_address-1.0-1.4.0.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/archive_mail.1.2-1.4.2.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/auto_cc-2.0-1.2.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/autocomplete.2.0-1.0.0.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/autosubscribe-1.1-1.4.2.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/bounce-0.5-1.4.x.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/compatibility-2.0.13-1.0.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/compose_chars-0.1-1.4.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/dictionary-0.6.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/folder_settings-0.3-1.4.0.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/folder_sizes-1.5-1.4.0.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/folder_synch.0.8-1.4.0.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/jump_to_folder.0.3-1.2.7.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/legend.1.2-1.2.8.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/limit_languages-1.0-1.4.0.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/login_notes-1.2-1.4.0.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/mark_read-1.4.2-1.2.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/notify_1_3.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/pupdate.0.7-1.4.2.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/quicksave-2.4.2-1.2.9.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/select_range-3.5.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/show_headers-1.3-1.4.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/spam_buttons-1.0-1.4.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/startup_folder-2.1-1.4.0.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/timeout_user-1.1.1-0.5.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/twc_weather-1.3p3b-RC2.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/user_special_mailboxes.0.1-1.4.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/variable_sent_folder.0.4-1.4.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/view_as_html-3.6-1.4.x.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/restrict_senders-1.5beta3-1.4.1.tar.gz | tar -xf - 
gzip -dc %{_sourcedir}/lockout-1.6-1.4.1.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/preview_pane-1.2-1.4.3.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/image_buttons-1.4-1.4.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/msg_flags-1.4.15a-1.4.3.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/squirrel_logger-2.3beta2-1.2.7.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/verify_reply_to-1.0-2.8.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/generic_info.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/empty_folders-2.0-1.2.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/login_activity-1.0-1.4.0.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/forced_prefs-1.4.sm-1.4.0.tar.gz | tar -xf -

%__patch --no-backup-if-mismatch -p0 < %PATCH4
%__patch --no-backup-if-mismatch -p0 < %PATCH5
%__patch --no-backup-if-mismatch -p0 < %PATCH7
%__patch --no-backup-if-mismatch -p1 < %PATCH9
%__patch --no-backup-if-mismatch -p1 < %PATCH16
cd ..
tar -xf %{_sourcedir}/rulogin.tar

cd src/
%__patch --no-backup-if-mismatch -p0 < %PATCH18

cd ..

patch --no-backup-if-mismatch -p0 < plugins/autocomplete/patch/sm-1.4.6.diff

patch --no-backup-if-mismatch -p0 < plugins/preview_pane/patches/preview_pane_squirrelmail-1.4.3.diff

cp plugins/preview_pane/source_files/archive_mail_bottom.php-1.2 plugins/archive_mail/includes/archive_mail_bottom.php

cd functions/

patch --no-backup-if-mismatch -p0 < ../plugins/image_buttons/sm14x.diff

cd ../plugins/twc_weather
%__patch --no-backup-if-mismatch -p1 < %PATCH11

cd ../verify_reply_to
%__patch --no-backup-if-mismatch -p1 < %PATCH17

cd ../image_buttons
%__patch --no-backup-if-mismatch -p1 < %PATCH13
%__patch --no-backup-if-mismatch -p0 < %PATCH20

cd ../msg_flags
patch --no-backup-if-mismatch -p0 < patches/msg_flags-squirrelmail-1.4.15.diff

%build
echo Nothing to do

%install
rm -rf %{buildroot}
mkdir -p -m0755 %{buildroot}%{sqmaildir}/data-words
mkdir -p -m0755 %{buildroot}%{sqmaildir}/local

#install -m0644 .htaccess    %{buildroot}%{sqmaildir}
install -m0644 AUTHORS      %{buildroot}%{sqmaildir}
install -m0644 ChangeLog    %{buildroot}%{sqmaildir}
install -m0644 configure    %{buildroot}%{sqmaildir}
install -m0644 COPYING      %{buildroot}%{sqmaildir}
#install -m0644 favicon.ico  %{buildroot}%{sqmaildir}
install -m0644 index.php    %{buildroot}%{sqmaildir}
install -m0644 INSTALL      %{buildroot}%{sqmaildir}
install -m0644 README       %{buildroot}%{sqmaildir}
install -m0644 ReleaseNotes %{buildroot}%{sqmaildir}
install -m0644 UPGRADE      %{buildroot}%{sqmaildir}

# copy over the rest
for d in class config contrib data doc functions help images include locale plugins po src themes templates; do
    cp -rp $d %{buildroot}%{sqmaildir}
done

chmod 755 %{buildroot}/%{sqmaildir}
chmod 755 %{buildroot}/%{sqmaildir}/plugins

# remove unpackaged files
rm -rf %{buildroot}/%{sqmaildir}/plugins/demo
rm -rf %{buildroot}/%{sqmaildir}/plugins/test

%clean

%post
cat << END
==========================NOTICE========================
Please ensure you have installed squirrelmail-%{version}-php4/php5
to pull down dependant packages.

You need to create a link from your web directory to the
squirrelmail directory.

Ex: ln -s %{sqmaildir} /usr/local/apache/htdocs/squirrelmail

Also, you will need to make a link from the webtools directory to ispell.

Ex: ln -s /usr/local/bin/ispell /usr/local/webtools/webbin/ispell

IMPORTANT: In order for sqmail to function you must copy
config_default.php to config.php and configure to your needs.
This package does not come preconfigured.

Ex: cp squirrelmail-%{version}/config/config_default.php \\
	squirrelmail-%{version}/config/config.php

Please read the INSTALL file for installation and info
regarding the spamfilter webtool.

Some plugins may need to be linked to their proper config files.
==========================NOTICE========================
END

%files
%defattr(-,www,www,755)
%doc %{sqmaildir}/AUTHORS
%doc %{sqmaildir}/ChangeLog
%doc %{sqmaildir}/COPYING
%doc %{sqmaildir}/INSTALL
%doc %{sqmaildir}/README
%doc %{sqmaildir}/ReleaseNotes
%doc %{sqmaildir}/UPGRADE 
%doc %{sqmaildir}/doc
#%{sqmaildir}/.htaccess
%{sqmaildir}/configure
#%{sqmaildir}/favicon.ico
%{sqmaildir}/index.php
%{sqmaildir}/class
%dir %{sqmaildir}
%dir %{sqmaildir}/plugins
%dir %{sqmaildir}/config
%config(noreplace) %{sqmaildir}/config/*
%config(noreplace) %{sqmaildir}/plugins/abook_import_export/config_default.php
#%config(noreplace) %{sqmaildir}/plugins/addgraphics/config.php
#%config(noreplace) %{sqmaildir}/plugins/folder_sizes/folder_sizes_config.php
#%config(noreplace) %{sqmaildir}/plugins/limit_languages/config.php
#%config(noreplace) %{sqmaildir}/plugins/login_notes/config.php
#%config(noreplace) %{sqmaildir}/plugins/mark_read/config.php
#%config(noreplace) %{sqmaildir}/plugins/pupdate/config.php
#%config(noreplace) %{sqmaildir}/plugins/quicksave/config.php
#%config(noreplace) %{sqmaildir}/plugins/select_range/config.php
#%config(noreplace) %{sqmaildir}/plugins/startup_folder/config.php
%config(noreplace) %{sqmaildir}/plugins/timeout_user/config.php
#%config(noreplace) %{sqmaildir}/plugins/twc_weather/config.php
%config(noreplace) %{sqmaildir}/plugins/webtools/config.php
%{sqmaildir}/plugins/webtools/quota/quota.php
%config(noreplace) %{sqmaildir}/plugins/webtools/serversidefilter/config.php
%config(noreplace) %{sqmaildir}/plugins/webtools/serversidefilter/setup.php
%config(noreplace) %{sqmaildir}/plugins/spam_buttons/config.php.sample
#%config(noreplace) %{sqmaildir}/.htaccess
%{sqmaildir}/contrib
%dir %{sqmaildir}/data
%{sqmaildir}/data/.htaccess
%config(noreplace) %{sqmaildir}/data/*
%{sqmaildir}/functions
%{sqmaildir}/help
%{sqmaildir}/images
%{sqmaildir}/include
%{sqmaildir}/locale
%{sqmaildir}/local
%{sqmaildir}/po
%{sqmaildir}/src
%{sqmaildir}/themes
%{sqmaildir}/templates
%{sqmaildir}/plugins/administrator
%{sqmaildir}/plugins/bug_report
%{sqmaildir}/plugins/calendar
%{sqmaildir}/plugins/delete_move_next
%{sqmaildir}/plugins/filters
%{sqmaildir}/plugins/fortune
%{sqmaildir}/plugins/index.php
%{sqmaildir}/plugins/info
%{sqmaildir}/plugins/listcommands
%{sqmaildir}/plugins/mail_fetch
# not found in 1.4.9a
#%{sqmaildir}/plugins/make_archive.pl
%{sqmaildir}/plugins/message_details
%{sqmaildir}/plugins/newmail
%{sqmaildir}/plugins/README.plugins
%{sqmaildir}/plugins/sent_subfolders
%{sqmaildir}/plugins/spamcop
%{sqmaildir}/plugins/squirrelspell
%{sqmaildir}/plugins/translate


%files plugins
%defattr(-,www,www,755)
%{sqmaildir}/plugins/abook_group
%{sqmaildir}/plugins/abook_import_export
%{sqmaildir}/plugins/addgraphics
%{sqmaildir}/plugins/add_address
%{sqmaildir}/plugins/archive_mail
%{sqmaildir}/plugins/auto_cc
%{sqmaildir}/plugins/autocomplete
%{sqmaildir}/plugins/autosubscribe
%{sqmaildir}/plugins/bounce
%{sqmaildir}/plugins/compatibility
%{sqmaildir}/plugins/compose_chars
%{sqmaildir}/plugins/dictionary
%{sqmaildir}/plugins/empty_folders
%{sqmaildir}/plugins/folder_settings
%{sqmaildir}/plugins/folder_sizes
%{sqmaildir}/plugins/folder_synch
%{sqmaildir}/plugins/forced_prefs
%{sqmaildir}/plugins/jump_to_folder
%{sqmaildir}/plugins/legend
%{sqmaildir}/plugins/limit_languages
%{sqmaildir}/plugins/lockout
%{sqmaildir}/plugins/login_notes
%{sqmaildir}/plugins/login_activity
%{sqmaildir}/plugins/mark_read
%{sqmaildir}/plugins/msg_flags
%{sqmaildir}/plugins/notify
%{sqmaildir}/plugins/preview_pane
%{sqmaildir}/plugins/pupdate
%{sqmaildir}/plugins/quicksave
%{sqmaildir}/plugins/restrict_senders
%{sqmaildir}/plugins/select_range
%{sqmaildir}/plugins/show_headers
%{sqmaildir}/plugins/spam_buttons
%{sqmaildir}/plugins/squirrel_logger
%{sqmaildir}/plugins/startup_folder
%{sqmaildir}/plugins/timeout_user
%{sqmaildir}/plugins/twc_weather
%{sqmaildir}/plugins/user_special_mailboxes
%{sqmaildir}/plugins/variable_sent_folder
%{sqmaildir}/plugins/verify_reply_to
%{sqmaildir}/plugins/view_as_html

%files webtools-plugins
%defattr(-,www,www,755)
%dir %{sqmaildir}/plugins/webtools
%{sqmaildir}/plugins/webtools/*

%files ru-plugins
%defattr(-,www,www,755)
%{sqmaildir}/plugins/image_buttons
%{sqmaildir}/plugins/generic_info

%files geoip 
%defattr(-,www,www,755)

%changelog
* Fri Jan 08 2010 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.4.16-13
- Webtool restoremail updated to copy messages from snapshot (instead of
  linking them).
* Tue Oct 20 2009 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.4.16-3
- Fixed newline in forward vacation.
* Wed Sep 30 2009 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.4.16-2
- Added local directory for RUPPB.
* Thu Jun 30 2009 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.4.16-1
- Added spam filter tweaks.
* Mon Sep 30 2008 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.4.16-1
- Updated to 1.4.16-1
- Removed plugins/abook_take
- Removed address_add plugin and added add_address plugin
* Wed Sep 17 2008 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.4.15-5
- Minor bugfixes in login_activity.
* Wed Sep 17 2008 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.4.15-4
- Added forced preferences 
- Removed show_user_ip plugin and plugin_show_user_ip patch
- Removed refresh_folder_values.patch
* Wed Sep 17 2008 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.4.15-4
- Fixed path in login.php
- Fixed flag bug in login_activity
* Tue Sep 16 2008 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.4.15-3
- Cleaned up login_activity plugin
- Added details link to campus status
- Integrated squirrel logger into login_activity and removed patch
- Fix maxcharacters of password field
* Wed Sep 3 2008 Aaron Richton <richton@nbcs.rutgers.edu> - 1.4.15-2
- Fix sqmaildir to use %{version} instead of hardcoded
* Mon Sep 1 2008 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.4.13-11
- Added favicon patch
- New login_notes plugin and patch
- New restrict senders plugin
- New squirrel_logger plugin and patch
- New empty_folders
- Added login_activity
- New compatibility
- New image_buttons
- Added check-criteria to webtools
- New image_buttons
- Applied login_page patch
* Mon Jul 14 2008 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.4.13-9
- Added empty_foldersbeta1 and new compatability plugin. 
- Removed left_frame.ptach and added long_folder_names.patch. 
* Thu Jul 3 2008 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.4.13-8
- Removed form tags to fix IE, Opera, Netscape bug in delete_purge all plugin.
* Thu Jun 26 2008 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.4.13-6
- Added delete purge all buttons plugin.
- Added generic info plugin and removed from webtools.
- Fixed p-error log warnings.
- Patched left frame folders ellipses and purge button for ADS.
- Updated restrict_senders to 1.5-1.4.1.
* Thu May 22 2008 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.4.13-3
- Fixed removal of tilde files.
- Fixed quota index.php.
* Mon May 19 2008 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.4.13-1
- Changed restoremail to restore from .snapshot rather than maildir.
- Fixed forward to self issue.
- Fixed newline issue in vacation subject.
- Updated restrict senders,compatibility,address group plugin, addressbook import
  export, mark read, show headers, startup folder, folder sizes, lockout.
- Added and tweaked show_user_and_ip, verify_reply_to, squirrel_logger.
- Updated relative path to redirect page when within Webtools plugin area.
- Added plugin to display important campus information in order to help ensure
  that webmail users are informed with the latest campus updates.
- Show "Contact Rutgers help Desk..." link which when clicked opens then 
  compose window in webmail with To: and Subject: filled in.
- Removed OLD index.php replacing with default index.php that is in every other
  plugin.
- Added includes for misc dir, campus_status dir.
- Added GeoIP (capture client IP country code/name), stateful last login info,
  RU custom formatting.
- Adds GeoIP (log client IP country code).
* Tue Oct 30 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.4.10.a-14
- Fixed msg_flags patching.
* Wed Oct 24 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.4.10.a-13
- Added msg_flags, fixed twc_weater & image_buttons, updated restrict senders,
  upgraded compatibility, updated quiksave, consolidated patches
  applied all forward-vacation/restoremail/quota fixes to code.
* Thu Aug 30 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.4.10.a-11
- Added boldoptions, fixed restoremail and forwardvacation.
* Fri Aug 24 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.4.10.a-10
- Fixed rpm wetools bugs
* Tue Aug 07 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.4.10.a-9
- Fixed restore mail bugs
* Wed Jul 18 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.4.10.a-8
- Updated quota plugin and fixed vacation subject box
* Tue Jul 17 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.4.10.a-7
- Removed mailfilter-old and fixed vacation/forward bugs
* Mon Jun 04 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.4.10.a-6
- Patched TWC Weather
* Mon Jun 04 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.4.10.a-5
- Added vacation and restoremail patches
* Mon Jun 04 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.4.10.a-4
- Fixing some perms
* Mon Jun 04 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.4.10.a-3
- Created new ru-plugin package
- Added new default patch
* Mon May 21 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.4.10.a-2
- Fixed the install path
* Mon May 21 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.4.10.a-1
- Version bump.
* Wed May 09 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.4.9.a-6
- Patched quota and spamfilter
- Added info message for spamfilter
* Fri Apr 27 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.4.9.a-5
- Added updated restricted senders plugin
- Added lockout plugin
- Added preview pane plugin
* Thu Apr 12 2007 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.4.9a-4
- Added restricted senders plugin
* Mon Jan 22 2007 John M. Santel <jmsl@nbcs.rutgers.edu> - 1.4.9a-1
- Bumped version to 1.4.9a, upgraded squirrelmail-1.4.8.patch to squirrelmail-1.4.9a.patch so it would apply cleanly
* Wed Oct 25 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.4.8-11
- Made another change in the spam_buttons patch, the patch was updated to include the mysteriously missing $spam_folder variable that allows the spam/not spam link to work correctly.
* Tue Oct 24 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.4.8-10
- Changed which patch spam_buttons uses
* Thu Oct 19 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.4.8-9
- Patched forward-vacation plugin
- Added autosubscribe plugin
- Added spam_buttons plugin, created a patch for it
- Updated abook_group plugin to 0.51
* Tue Oct 03 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.4.8-8
- Really updated the abook_group plugin
- Added two files as config
- Added hushquota plugin, patched webtools for hushquota
- Patched forward-vacation plugin
* Thu Sep 28 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.4.8-7
- Upgraded abook_group plugin from 0.50 to 0.51rc1.
- Changed certain config files to be treated as such in the spec
  file.
- umask 022 problem fixed.
- Added this Changelog-RU file.
* Fri Sep 08 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.4.8-6
- /usr/local/squirrelmail-1.4.8/plugins/webtools/config.php was
  munged and is now fixed.
- Fixed the %post output (willl -> will) and
  (/usr/local/webtools/bin/ispell -> /usr/local/webtools/webbin/ispell).
- Fixed the perms in spec for /usr/local/squirrelmail-1.4.8/ and
  /usr/local/squirrelmail-1.4.8/plugins/ to be www:www and 755.
* Thu Sep 07 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.4.8-5
- Patch the webtools spamfilter plugin to account for auto
  spamfiltering being turned on (5* and 30 days until expunged).
- Add/Patch autocomplete functionality (autocomplete.diff is the
  patch file).
* Wed Sep 06 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.4.8-3
- Made LDAP search smarter
* Mon Jul 31 2006 Eric Rivas <kc2hmv@nbcs.rutgers.edu> - 1.4.7-2
- Update to squirrelmail-1.4.7.
* Thu Mar 09 2006 Jonathan Kaczynski <jmkacz@oss.rutgers.edu> - 1.4.6-1ru
- Upgraded to latest version.
- Updated patch file.
* Fri Feb 03 2006 Jonathan Kaczynski <jmkacz@oss.rutgers.edu> - 1.4.5-1ru
- Upgraded to latest version.
