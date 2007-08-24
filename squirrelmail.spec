%define sqmaildir /usr/local/squirrelmail-1.4.10a

Summary:	SquirrelMail webmail client (Rutgers customized)
Name:		squirrelmail
Version:	1.4.10a
Release:	10
License:	GPL
Group:		Applications/Internet
Source:		%{name}-%{version}.tar.bz2
Source1: 	webmail-webtools.tar
Source2: 	abook_group-0.51-1.4.2.tar.gz
Source3: 	abook_import_export-0.9-1.4.0.tar.gz
Source4: 	addgraphics-2.3-1.0.3.tar.gz
Source5: 	address_add-2.1-1.4.0.tar.gz
Source6: 	archive_mail.1.2-1.4.2.tar.gz
Source7: 	auto_cc-2.0-1.2.tar.gz
Source8: 	autocomplete.2.0-1.0.0.tar.gz
Source9: 	bounce-0.5-1.4.x.tar.gz
Source10: 	compatibility-2.0.4.tar.gz
Source11: 	compose_chars-0.1-1.4.tar.gz
Source12: 	dictionary-0.6.tar.gz
Source13: 	folder_settings-0.3-1.4.0.tar.gz
Source14: 	folder_sizes.1.4-1.4.tar.gz
Source15: 	folder_synch.0.8-1.4.0.tar.gz
Source16: 	jump_to_folder.0.3-1.2.7.tar.gz
Source17: 	legend.1.2-1.2.8.tar.gz
Source18: 	limit_languages-1.0-1.4.0.tar.gz
Source19: 	login_notes-1.1-1.4.0.tar.gz
Source20: 	mark_read.1.4.1-1.4.2.tar.gz
Source21: 	notify_1_3.tar.gz
Source22: 	pupdate.0.7-1.4.2.tar.gz
Source23: 	quicksave-2.3-1.1.0.tar.gz
Source24: 	select_range-3.5.tar.gz
Source25: 	serversidefilter-1.42.tar.gz
Source26: 	show_headers-1.2-1.4.tar.gz
Source27: 	startup_folder-2.0-1.4.0.tar.gz
Source28: 	timeout_user-1.1.1-0.5.tar.gz
Source29: 	twc_weather-1.3p2-rc1.tar.gz
Source30: 	user_special_mailboxes.0.1-1.4.tar.gz
Source31: 	variable_sent_folder.0.4-1.4.tar.gz
Source32: 	view_as_html-3.6-1.4.x.tar.gz
Source33: 	autosubscribe-1.1-1.4.2.tar.gz 
Source34: 	spam_buttons-1.0-1.4.tar.gz
Source35: 	restrict_senders-1.2-1.4.1.tar.gz
Source36: 	lockout-1.4-1.4.1.tar.gz
Source37: 	preview_pane-1.2-1.4.3.tar.gz
Source38:	generic_header-1.0-1.4.tar.gz
Source39:	image_buttons-1.4-1.4.tar.gz
Patch1: 	squirrelmail.patch
Patch2:		squirrelmail-plugins-1.4.8.patch
Patch3:		squirrelmail-ldapfix.patch
Patch4: 	autocomplete.diff
Patch5: 	spambuttons.patch
Patch6: 	vacation.patch
Patch7:		twc_weather.patch
Patch8: 	mailfilter.patch
Patch9:		restoremail.patch
Patch10:	quotasubject.patch 
URL: 		http://www.squirrelmail.org/
Vendor: 	NBCS-OSS
Packager: 	Naveen Gavini <ngavini@nbcs.rutgers.edu>
BuildRoot: 	%{_tmppath}/%{name}-root
Requires: 	apache-module-php
Requires: 	apache
Requires: 	perl
Requires: 	ispell
Requires: 	courier-imap
Requires: 	webtools

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
Requires:	%{name} = %{version}

%description plugins
abook_group-0.51-1.4.2         - Address Group Plugin
abook_import_export-0.9-1.4.0  - Addressbook Import-Export
addgraphics-2.3-1.0.3          - Add Graphics
address_add-2.1-1.4.0          - Address Add
archive_mail-1.2-1.4.2         - Archive Mail
auto_cc-2.0-1.2                - Auto CC
autocomplete.2.0-1.0.0         - Autocomplete
autosubscribe-1.1-1.4.2        - Autosubscribe
bounce-0.5-1.4.x               - Bounce
compatibility-2.0.4            - Compatibility
compose_chars-0.1-1.4          - Compose Special Characters
dictionary-0.6                 - Dictionary
folder_settings-0.3-1.4.0      - Folder Settings
folder_sizes.1.4-1.4           - Folder Sizes
folder_synch.0.8-1.4.0         - Folder Synch
jump_to_folder.0.3-1.2.7       - Jump to Folder
legend.1.2-1.2.8               - Highlighting Legend
limit_languages-1.0-1.4.0      - Limit Languages
lockout-1.4-1.4.1              - Lockout
login_notes-1.1-1.4.0          - Login Notes
mark_read.1.4.1-1.4.2          - Mark Read
notify_1_3                     - Notify New Mail Popup
preview_pane-1.2-1.4.3         - Preview Pane
pupdate.0.7-1.4.2              - Plugin Updates
quicksave-2.3-1.1.0            - Quick Save
select_range-3.5               - Select Range
restrict_senders-1.2-1.4.1     - Restricted Senders
serversidefilter-1.42          - Server Side Filter
show_headers-1.2-1.4           - Show Headers
spam_buttons-1.0-1.4           - Spam Buttons
startup_folder-2.0-1.4.0       - Startup Folder
timeout_user-1.1.1-0.5         - Timeout User
twc_weather-1.3p2-rc1          - TWC Weather
user_special_mailboxes.0.1-1.4 - User Special Mailboxes
variable_sent_folder.0.4-1.4   - Variable Sent Folder
view_as_html-3.6-1.4.x         - View as HTML

%package webtools-plugins
Summary:	SquirrelMail webtools plugins
Group:		Applications/Internet
Requires:       %{name} = %{version}

%description webtools-plugins
webtools

%package ru-plugins
Summary:	SquirrelMail webtools plugins
Group:		Applications/Internet
Requires:       %{name} = %{version}

%description ru-plugins
Rutgers home-grown Squirrelmail Plugins

generic_header-1.0-1.4
image_buttons-1.4-1.4

%prep
PATH="/usr/local/gnu/bin:/usr/local/bin:/usr/sfw/bin:$PATH"
export PATH

%setup -q
%patch1 -p1
%patch3 -p1

cd plugins
tar -xf %{_sourcedir}/webmail-webtools.tar
gzip -dc %{_sourcedir}/abook_group-0.51-1.4.2.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/abook_import_export-0.9-1.4.0.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/addgraphics-2.3-1.0.3.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/address_add-2.1-1.4.0.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/archive_mail.1.2-1.4.2.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/auto_cc-2.0-1.2.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/autocomplete.2.0-1.0.0.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/autosubscribe-1.1-1.4.2.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/bounce-0.5-1.4.x.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/compatibility-2.0.4.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/compose_chars-0.1-1.4.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/dictionary-0.6.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/folder_settings-0.3-1.4.0.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/folder_sizes.1.4-1.4.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/folder_synch.0.8-1.4.0.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/jump_to_folder.0.3-1.2.7.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/legend.1.2-1.2.8.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/limit_languages-1.0-1.4.0.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/login_notes-1.1-1.4.0.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/mark_read.1.4.1-1.4.2.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/notify_1_3.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/pupdate.0.7-1.4.2.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/quicksave-2.3-1.1.0.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/select_range-3.5.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/serversidefilter-1.42.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/show_headers-1.2-1.4.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/spam_buttons-1.0-1.4.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/startup_folder-2.0-1.4.0.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/timeout_user-1.1.1-0.5.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/twc_weather-1.3p2-rc1.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/user_special_mailboxes.0.1-1.4.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/variable_sent_folder.0.4-1.4.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/view_as_html-3.6-1.4.x.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/restrict_senders-1.2-1.4.1.tar.gz | tar -xf - 
gzip -dc %{_sourcedir}/lockout-1.4-1.4.1.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/preview_pane-1.2-1.4.3.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/generic_header-1.0-1.4.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/image_buttons-1.4-1.4.tar.gz | tar -xf -

%patch2 -p1

%patch4 -p1
%patch8 -p0
%patch9 -p0
%patch10 -p0
cd ..

%patch5 -p3

patch -p0 < plugins/autocomplete/patch/sm-1.4.6.diff

patch -p0 < plugins/preview_pane/patches/preview_pane_squirrelmail-1.4.3.diff

cp plugins/preview_pane/source_files/archive_mail_bottom.php-1.2 plugins/archive_mail/includes/archive_mail_bottom.php

cd functions/

patch -p0 < ../plugins/image_buttons/sm1410a.diff

cd ..
cd plugins/

cd twc_weather
%patch7 -p0


%build
echo Nothing to do

%install
rm -rf %{buildroot}
mkdir -p -m0755 %{buildroot}%{sqmaildir}/data-words

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
for d in class config contrib data doc functions help images include locale plugins po src themes; do
    cp -rp $d %{buildroot}%{sqmaildir}
done

chmod 755 %{buildroot}/%{sqmaildir}
chmod 755 %{buildroot}/%{sqmaildir}/plugins

%clean
rm -rf %{buildroot}

%post
cat << END
==========================NOTICE========================
You need to create a link from your web directory to the
squirrelmail directory.

Ex: ln -s %{sqmaildir} /usr/local/apache/htdocs/squirrelmail

Also, you will need to make a link from the webtools directory to ispell.

Ex: ln -s /usr/local/bin/ispell /usr/local/webtools/webbin/ispell

IMPORTANT: In order for sqmail to function you must copy
config_default.php to config.php and configure to your needs.
This package does not come preconfigured.

Ex: cp squirrelmail-1.4.10a/config/config_default.php \\
	squirrelmail-1.4.10a/config/config.php

Please read the INSTALL file for installation and info
regarding the spamfilter webtool.

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
%config(noreplace) %{sqmaildir}/plugins/addgraphics/config.php
%config(noreplace) %{sqmaildir}/plugins/folder_sizes/folder_sizes_config.php
%config(noreplace) %{sqmaildir}/plugins/limit_languages/config.php
%config(noreplace) %{sqmaildir}/plugins/login_notes/config.php
%config(noreplace) %{sqmaildir}/plugins/mark_read/config.php
%config(noreplace) %{sqmaildir}/plugins/pupdate/config.php
%config(noreplace) %{sqmaildir}/plugins/quicksave/config.php
%config(noreplace) %{sqmaildir}/plugins/select_range/config.php
%config(noreplace) %{sqmaildir}/plugins/serversidefilter/config.php
%config(noreplace) %{sqmaildir}/plugins/serversidefilter/setup.php
%config(noreplace) %{sqmaildir}/plugins/startup_folder/config.php
%config(noreplace) %{sqmaildir}/plugins/timeout_user/config.php
%config(noreplace) %{sqmaildir}/plugins/twc_weather/config.php
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
%{sqmaildir}/po
%{sqmaildir}/src
%{sqmaildir}/themes
%{sqmaildir}/plugins/abook_take
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
%{sqmaildir}/plugins/address_add
%{sqmaildir}/plugins/archive_mail
%{sqmaildir}/plugins/auto_cc
%{sqmaildir}/plugins/autocomplete
%{sqmaildir}/plugins/autosubscribe
%{sqmaildir}/plugins/bounce
%{sqmaildir}/plugins/compatibility
%{sqmaildir}/plugins/compose_chars
%{sqmaildir}/plugins/dictionary
%{sqmaildir}/plugins/folder_settings
%{sqmaildir}/plugins/folder_sizes
%{sqmaildir}/plugins/folder_synch
%{sqmaildir}/plugins/jump_to_folder
%{sqmaildir}/plugins/legend
%{sqmaildir}/plugins/limit_languages
%{sqmaildir}/plugins/lockout
%{sqmaildir}/plugins/login_notes
%{sqmaildir}/plugins/mark_read
%{sqmaildir}/plugins/notify
%{sqmaildir}/plugins/preview_pane
%{sqmaildir}/plugins/pupdate
%{sqmaildir}/plugins/quicksave
%{sqmaildir}/plugins/restrict_senders
%{sqmaildir}/plugins/select_range
%{sqmaildir}/plugins/serversidefilter
%{sqmaildir}/plugins/show_headers
%{sqmaildir}/plugins/spam_buttons
%{sqmaildir}/plugins/startup_folder
%{sqmaildir}/plugins/timeout_user
%{sqmaildir}/plugins/twc_weather
%{sqmaildir}/plugins/user_special_mailboxes
%{sqmaildir}/plugins/variable_sent_folder
%{sqmaildir}/plugins/view_as_html

%files webtools-plugins
%defattr(-,www,www,755)
%dir %{sqmaildir}/plugins/webtools
%{sqmaildir}/plugins/webtools/*

%files ru-plugins
%defattr(-,www,www,755)
%{sqmaildir}/plugins/image_buttons
%{sqmaildir}/plugins/generic_header

%changelog
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
