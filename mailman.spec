Summary:      Mailing list
Name:         mailman
Version:      2.1.13
Release:      1
License:      GPL
Group:        Applications/Mail
Source0:      http://ftp.gnu.org/gnu/mailman/mailman-%{version}.tgz
URL:          http://www.gnu.org/software/mailman/mailman.html
Distribution: RU-Solaris
Vendor:       NBCS-OSS
BuildRoot:    %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:     python

%description
Mailman is software to help manage email discussion lists, much like Majordomo
and SmartList. Unlike most similar products, Mailman gives each mailing list a
web page, and allows users to subscribe, unsubscribe, etc. over the web. Even 
the list manager can administer his or her list entirely from the web. Mailman
also integrates most things people want to do with mailing lists, including 
archiving, mail-to-news gateways, integrated bounce handling, spam prevention,
email-based admin commands, direct SMTP delivery (with fast bulk mailing), 
support for virtual domains, and more. 
%prep
%setup -q

%build
%configure --prefix=%{_prefix}/mailman --without-permcheck
gmake

%install
gmake install DESTDIR=$RPM_BUILD_ROOT

%pre
#Checking for user and group mailman
echo "Checking system for user and group mailamn."

/usr/local/gnu/bin/grep "^mailman:" /etc/group

if [ "$?" == "0" ]; then \
	echo "Group mailman found, great."; \
else
	echo "MAILMAN GROUP NOT FOUND, RPM INSTALLATION"
	echo "SELF DESTRUCTING.  YOU MAY NEED TO REBUILD"
	echo "YOUR RPM DATABASE AND REMOVE TEMP FILES."
	echo "YOU SHOULD HAVE PROBABLY SEEN THIS COMING."
	echo "NOW, THIS RPM WILL PAUSE FOR 30 SECONDS OF"
	echo "SILENCE BEFORE THIS PROCESS SELF DESTRUCTS."
	sleep 30
	echo "^GRPM DYING NOW!"
	sleep 5
	echo "Executing command 'kill $PPID', goodbye!"
	kill -9 $PPID;
fi

/usr/local/gnu/bin/grep "^mailman:" /etc/passwd
if [ "$?" == "0" ]; then \
        echo "User mailman found, great."; \
else
	echo "MAILMAN GROUP NOT FOUND, RPM INSTALLATION"
        echo "SELF DESTRUCTING.  YOU MAY NEED TO REBUILD"
        echo "YOUR RPM DATABASE AND REMOVE TEMP FILES."
        echo "YOU SHOULD HAVE PROBABLY SEEN THIS COMING."
        echo "NOW, THIS RPM WILL PAUSE FOR 30 SECONDS OF"
        echo "SILENCE BEFORE THIS PROCESS SELF DESTRUCTS."
        sleep 30
        echo "^GRPM DYING NOW!"
        sleep 5
        echo "Executing command 'kill $PPID', goodbye!"
        kill -9 $PPID;
fi

%post
#echo You may need to add a mailman group and user

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,mailman,mailman)
%doc BUGS FAQ INSTALL NEWS README*
/usr/local/mailman/

%changelog
* Thu Aug 05 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 2.1.13-1
- Update to the latest version
