%define name logtools
%define version 0.13a
%define release 4
%define prefix /usr/local

Summary: The Logtools package contains a number of programs for managing log files.
Name: %name
Version: %version
Release: %release
Copyright: Russel Coker
Group: Logtools
Source0: http://www.coker.com.au/logtools/logtools-0.13a.tar.gz
BuildRoot: /var/local/tmp/%{name}-root

%description
--clfmerge will merge a number of Common Logfile Format web log files into a single file while also re-ordering them in a sliding window to cope with web servers that generate log entries with the start-time of the request and write them in order of completion. 
--logprn operates like tail -f but will (after a specified period of inactivity) spawn a process and write the new data in the log file to it's standard input. 
--clfsplit will split up a single CLF format web log into a number of files based on the client's IP address.      
--funnel will write it's standard-input to a number of files or processes. 
--clfdomainsplit split a CLF format web log containing fully qualified URLs (including the host name) into separate files, one for each host.

%prep
%setup 


%build
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" ./configure --prefix=%{prefix} --mandir=$RPM_BUILD_ROOT%{prefix}/man
cd sun
make  INSTROOT=$RPM_BUILD_ROOT%{prefix} 

%install
mv $RPM_BUILD_ROOT%{prefix}/etc/clfdomainsplit.cfg $RPM_BUILD_ROOT%{prefix}/etc/clfdomainsplit.cfg.rpm


%post 
echo mv /usr/local/etc/clfdomainsplit.cfg.rpm /usr/local/etc/clfdomainsplit.cfg in order to use it!

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0755, root, root)
%doc bulk-virtual-webalizer.txt sample-webalizer.conf getweblogs
%{prefix}/bin/*
%attr(0644, root,root)%{prefix}/etc/clfdomainsplit.cfg.rpm
%attr(0644, root,root)%{prefix}/man/man1/*

