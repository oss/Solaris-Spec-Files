Summary: tikiwiki - a powerful open source Content Management System (CMS)/ Groupware

Name: tikiwiki
Version: 1.7.1.1
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: %{name}_%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: apache
Requires: mysql
Requires: apache-module-php >= 4.3.1

%description
Tiki CMS/Groupware (aka TikiWiki) is a powerful open source Content Management System (CMS)/ Groupware that can be used to create all sorts of Web applications, Sites, Portals, Intranets and Extranets. TikiWiki is also works great as a web based collaboration tool. TikiWiki is a multi-purpose package with a lot of native options and sections that you can enable/disable as you need them. It is designed to be international, clean and extensible. TikiWiki incorporates all the features present in several excellent wiki systems available today plus a lot of new features and options, allowing your wiki application to be whatever you want it to be, from a simple wiki to a complex site for a whole user community with many intermediate steps, you can use TikiWiki as a forums site, a chatroom, polls, and much more! The possibilities are endless.

TikiWikis major features include: article, forum, newsletter, blog, file/image gallery, wiki, drawing, tracker, directory, poll/survey, quiz, FAQ, chat, banner, webmail, calendar, category, ACL, and more.

%prep

%build

%install
mkdir -p %{buildroot}/usr/local/src 
cd %{buildroot}/usr/local/src
gzip -dc /usr/local/src/rpm-packages/SOURCES/%{source} | tar -xf -

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat << EOF
****************** TikiWiki Installation notes ******************

This RPM only provides the TikiWiki source, and installs its 
dependencies. In order to fully install TikiWiki, you will 
need to read:

/usr/local/src/%{name}_%{version}/README 
/usr/local/src/%{name}_%{version}/INSTALL

Also:
--
* If you want to use uploads (files,images) make sure uploads are enabled in php.ini. 

file_uploads = On

* Tiki uses sessions (a common mechanism in PHP4) make sure that the path where PHP stores sessions (php.ini)
exists and that PHP can write to that path. 

session.save_handler = files
session.save_path = /tmp

* It is highly recommended to increase the maximum memory size for PHP scripts from 8Mb to 16Mb in your
php.ini configuration file. (Note from 1.6 Tiki MAY run in 8Mb environments) 

memory_limit = 16M

* Another settings I'd recommend to change which may cause timeouts if your wiki is large and prevent you
from doing a Backup through the Admin menu. 

max_execution_time = 60 
--

EOF

%files
%defattr(-,bin,bin)
# /usr/local/src/%{name}_%{version}

