
Summary: A widely used Mail Transport Agent (MTA)
Name: sendmail
Version: 8.14.2
Release: 1
License: Sendmail
Group: System Environment/Daemons
URL: http://www.sendmail.org/
Source0: %{name}.%{version}.tar.gz
Source1: site.config.m4
Provides: MTA smtpdaemon
Buildroot: /var/local/tmp/%{name}-%{version}-%{release}-root
Packager: David Diffenbaugh <davediff@nbcs.rutgers.edu>
BuildConflicts: gdbm

%description
The Sendmail program is a very widely used Mail Transport Agent (MTA).
MTAs send mail from one machine to another. Sendmail is not a client
program, which you use to read your email. Sendmail is a
behind-the-scenes program which actually moves your email over
networks or the Internet to where you want it to go.

If you ever need to reconfigure Sendmail, you will also need to have
the sendmail-cf package installed. If you need documentation on
Sendmail, you can install the sendmail-doc package.

%package milter
Summary: The sendmail milter addons
Group: Development/Libraries 
 
%description milter
Sendmail libmilter shared object file 

%package milter-devel
Summary: Extra development include files and development libraries 
Group: Development/Libraries

%description milter-devel
Include files and devel libraries for e.g. the milter addons as part
of sendmail.

%prep
%setup -q

%build
#need to create a site.config.m4 to let make know we want to use /opt/SUNWspro/bin/cc and to pass the -Kpic option
cp ../../SOURCES/site.config.m4 devtools/Site/

cd libsm
./Build
cd ../libsmutil
./Build
cd ../libmilter
./Build
cd ../obj.SunOS.5.9.sun4/libmilter
/opt/SUNWspro/bin/CC -G -o libmilter.so.1 -z text -z defs -B direct -z lazyload -z combreloc -z ignore -R /usr/local/lib -h libmilter.so.1 main.o engine.o listener.o handler.o comm.o smfi.o signal.o sm_gethost.o -L. -lc -lnsl -lsocket ../libsm/libsm.a -lresolv

%install

mkdir -p %{buildroot}/usr/local/lib/
mkdir -p %{buildroot}/usr/local/include/libmilter/

cd obj.SunOS.5.9.sun4/libmilter
/usr/local/gnu/bin/cp libmilter.so.1 libmilter.a ../libsmutil/libsmutil.a ../libsm/libsm.a %{buildroot}/usr/local/lib
/usr/local/gnu/bin/cp ../../include/libmilter/* %{buildroot}/usr/local/include/libmilter

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)

%files milter
%defattr(-,root,root)
/usr/local/lib/libmilter.so.1

%files milter-devel
%defattr(-,root,root)
%dir /usr/local/include/libmilter
/usr/local/include/libmilter/*.h
/usr/local/lib/libmilter.a
/usr/local/lib/libsmutil.a
/usr/local/lib/libsm.a

%changelog
* Fri Mar 07 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 8.14.2-1
- created libmilter package
