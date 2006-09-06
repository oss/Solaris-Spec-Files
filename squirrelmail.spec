%define sqmaildir /usr/local/squirrelmail-1.4.8

Summary: SquirrelMail webmail client (Rutgers customized)
Name: squirrelmail
Version: 1.4.8
Release: 3
Copyright: GPL
Group: Applications/Internet
Source: %{name}-%{version}.tar.bz2
Source1: webmail-webtools.tar
Source2: abook_group.0.50-1.4.2.tar.gz
Source3: abook_import_export-0.9-1.4.0.tar.gz
Source4: addgraphics-2.3-1.0.3.tar.gz
Source5: address_add-2.1-1.4.0.tar.gz
Source6: archive_mail.1.2-1.4.2.tar.gz
Source7: auto_cc-2.0-1.2.tar.gz
Source8: autocomplete.2.0-1.0.0.tar.gz
Source9: bounce-0.5-1.4.x.tar.gz
Source10: compatibility-2.0.4.tar.gz
Source11: compose_chars-0.1-1.4.tar.gz
Source12: dictionary-0.6.tar.gz
Source13: folder_settings-0.3-1.4.0.tar.gz
Source14: folder_sizes.1.4-1.4.tar.gz
Source15: folder_synch.0.8-1.4.0.tar.gz
Source16: jump_to_folder.0.3-1.2.7.tar.gz
Source17: legend.1.2-1.2.8.tar.gz
Source18: limit_languages-1.0-1.4.0.tar.gz
Source19: login_notes-1.1-1.4.0.tar.gz
Source20: mark_read.1.4.1-1.4.2.tar.gz
Source21: notify_1_3.tar.gz
Source22: pupdate.0.7-1.4.2.tar.gz
Source23: quicksave-2.3-1.1.0.tar.gz
Source24: select_range-3.5.tar.gz
Source25: serversidefilter-1.42.tar.gz
Source26: show_headers-1.2-1.4.tar.gz
Source27: startup_folder-2.0-1.4.0.tar.gz
Source28: timeout_user-1.1.1-0.5.tar.gz
Source29: twc_weather-1.3p2-rc1.tar.gz
Source30: user_special_mailboxes.0.1-1.4.tar.gz
Source31: variable_sent_folder.0.4-1.4.tar.gz
Source32: view_as_html-3.6-1.4.x.tar.gz
Patch1: squirrelmail-1.4.8.patch
Patch2: squirrelmail-plugins-1.4.7.patch
Patch3:	squirrelmail-ldapfix.patch
URL: http://www.squirrelmail.org/
Vendor: NBCS-OSS
Packager: Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-root
Requires: apache-module-php
Requires: apache
Requires: perl
Requires: ispell
Requires: courier-imap
Requires: webtools

%description
SquirrelMail is a standards-based Webmail package written in PHP4.
It includes built-in pure PHP support for the IMAP and SMTP protocols,
and all pages are rendered in pure HTML 4.0 for maximum compatibility
across browsers. It has very few requirements, and is very easy to
configure and install. It has all the functionality you would want
from an email client, including strong MIME support, address books,
and folder manipulation.

%package plugins
Summary: SquirrelMail plugins
Group: Applications/Internet

%description plugins
abook_group.0.50-1.4.2         - Address Group Plugin
abook_import_export-0.9-1.4.0  - Addressbook Import-Export
addgraphics-2.3-1.0.3          - Add Graphics
address_add-2.1-1.4.0          - Address Add
archive_mail-1.2-1.4.2         - Archive Mail
auto_cc-2.0-1.2                - Auto CC
autocomplete.2.0-1.0.0         - Autocomplete
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
login_notes-1.1-1.4.0          - Login Notes
mark_read.1.4.1-1.4.2          - Mark Read
notify_1_3                     - Notify New Mail Popup
pupdate.0.7-1.4.2              - Plugin Updates
quicksave-2.3-1.1.0            - Quick Save
select_range-3.5               - Select Range
serversidefilter-1.42          - Server Side Filter
show_headers-1.2-1.4           - Show Headers
startup_folder-2.0-1.4.0       - Startup Folder
timeout_user-1.1.1-0.5         - Timeout User
twc_weather-1.3p2-rc1          - TWC Weather
user_special_mailboxes.0.1-1.4 - User Special Mailboxes
variable_sent_folder.0.4-1.4   - Variable Sent Folder
view_as_html-3.6-1.4.x         - View as HTML

%package webtools-plugins
Summary: SquirrelMail webtools plugins
Group: Applications/Internet

%description webtools-plugins
webtools

%prep
PATH="/usr/local/gnu/bin:/usr/local/bin:/usr/sfw/bin:$PATH"
export PATH

%setup -q
%patch1 -p1
%patch3 -p1

cd plugins
tar -xf %{_sourcedir}/webmail-webtools.tar
gzip -dc %{_sourcedir}/abook_group.0.50-1.4.2.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/abook_import_export-0.9-1.4.0.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/addgraphics-2.3-1.0.3.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/address_add-2.1-1.4.0.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/archive_mail.1.2-1.4.2.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/auto_cc-2.0-1.2.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/autocomplete.2.0-1.0.0.tar.gz | tar -xf -
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
gzip -dc %{_sourcedir}/startup_folder-2.0-1.4.0.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/timeout_user-1.1.1-0.5.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/twc_weather-1.3p2-rc1.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/user_special_mailboxes.0.1-1.4.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/variable_sent_folder.0.4-1.4.tar.gz | tar -xf -
gzip -dc %{_sourcedir}/view_as_html-3.6-1.4.x.tar.gz | tar -xf -
%patch2 -p1

%build
echo Nothing to do

%install
rm -rf %{buildroot}
mkdir -p -m0755 %{buildroot}/%{sqmaildir}/
mkdir -p -m0755 %{buildroot}/%{sqmaildir}/data-words/

install -m0644 .htaccess    %{buildroot}/%{sqmaildir}/
install -m0644 AUTHORS      %{buildroot}/%{sqmaildir}/
install -m0644 ChangeLog    %{buildroot}/%{sqmaildir}/
install -m0644 configure    %{buildroot}/%{sqmaildir}/
install -m0644 COPYING      %{buildroot}/%{sqmaildir}/
install -m0644 favicon.ico  %{buildroot}/%{sqmaildir}/
install -m0644 index.php    %{buildroot}/%{sqmaildir}/
install -m0644 INSTALL      %{buildroot}/%{sqmaildir}/
install -m0644 README       %{buildroot}/%{sqmaildir}/
install -m0644 ReleaseNotes %{buildroot}/%{sqmaildir}/
install -m0644 UPGRADE      %{buildroot}/%{sqmaildir}/

# copy over the rest
for d in class config contrib data doc functions help images include locale plugins po src themes; do
    cp -rp $d %{buildroot}/%{sqmaildir}
done

%clean
rm -rf %{buildroot}

%post
cat << END
 __NOTICE__
You need to create a link from your web directory to the
squirrelmail directory.

Ex: ln -s %{sqmaildir} /usr/local/apache/htdocs/squirrelmail

Also, you willl need to make a link from the webtools directory to ispell.

Ex: ln -s /usr/local/bin/ispell /usr/local/webtools/bin/ispell

END

%files
%defattr(-,www,www)
%doc %{sqmaildir}/AUTHORS
%doc %{sqmaildir}/ChangeLog
%doc %{sqmaildir}/COPYING
%doc %{sqmaildir}/INSTALL
%doc %{sqmaildir}/README
%doc %{sqmaildir}/ReleaseNotes
%doc %{sqmaildir}/UPGRADE 
%doc %{sqmaildir}/doc
%{sqmaildir}/.htaccess
%{sqmaildir}/configure
%{sqmaildir}/favicon.ico
%{sqmaildir}/index.php
%{sqmaildir}/class
%dir %{sqmaildir}/config
%config(noreplace) %{sqmaildir}/config/*
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
%{sqmaildir}/plugins/make_archive.pl
%{sqmaildir}/plugins/message_details
%{sqmaildir}/plugins/newmail
%{sqmaildir}/plugins/README.plugins
%{sqmaildir}/plugins/sent_subfolders
%{sqmaildir}/plugins/spamcop
%{sqmaildir}/plugins/squirrelspell
%{sqmaildir}/plugins/translate


%files plugins
%defattr(-,www,www)
%{sqmaildir}/plugins/abook_group
%{sqmaildir}/plugins/abook_import_export
%{sqmaildir}/plugins/addgraphics
%{sqmaildir}/plugins/address_add
%{sqmaildir}/plugins/archive_mail
%{sqmaildir}/plugins/auto_cc
%{sqmaildir}/plugins/autocomplete
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
%{sqmaildir}/plugins/login_notes
%{sqmaildir}/plugins/mark_read
%{sqmaildir}/plugins/notify
%{sqmaildir}/plugins/pupdate
%{sqmaildir}/plugins/quicksave
%{sqmaildir}/plugins/select_range
%{sqmaildir}/plugins/serversidefilter
%config(noreplace) %{sqmaildir}/plugins/serversidefilter/config.php
%{sqmaildir}/plugins/show_headers
%{sqmaildir}/plugins/startup_folder
%{sqmaildir}/plugins/timeout_user
%{sqmaildir}/plugins/twc_weather
%{sqmaildir}/plugins/user_special_mailboxes
%{sqmaildir}/plugins/variable_sent_folder
%{sqmaildir}/plugins/view_as_html

%files webtools-plugins
%defattr(-,www,www)
%dir %{sqmaildir}/plugins/webtools
%{sqmaildir}/plugins/webtools/*

%changelog
* Wed Sep 06 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.4.8-3
- Made LDAP search smarter
* Mon Jul 31 2006 Eric Rivas <kc2hmv@nbcs.rutgers.edu> - 1.4.7-2
- Update to squirrelmail-1.4.7.
* Thu Mar 09 2006 Jonathan Kaczynski <jmkacz@oss.rutgers.edu> - 1.4.6-1ru
- Upgraded to latest version.
- Updated patch file.
* Fri Feb 03 2006 Jonathan Kaczynski <jmkacz@oss.rutgers.edu> - 1.4.5-1ru
- Upgraded to latest version.
