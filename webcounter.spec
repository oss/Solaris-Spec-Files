%define apver 1.3.26
%define apache_prefix /usr/local/apache-%{apver}

Summary: WebCounter apache module
Name: webcounter
Version: 2.3.0
Release: 3ru
Group: Applications/Internet
License: FSF
Source: http://www.dan.co.jp/webcounter/webcounter-latest.tar.gz
Source1: apache_%{apver}.tar.gz
Patch: webcounter.patch
BuildRoot: /var/tmp/%{name}-root
Provides: mod_cntr

BuildRequires: apache apache-devel
Requires: apache = %{apver}

%description
It's a webcounter for apache.

%prep
%setup -q -a0
%setup -q -a1
%patch -p1
cp -r $RPM_BUILD_DIR/webcounter-%{version}/cntr $RPM_BUILD_DIR/webcounter-%{version}/apache_%{apver}/src/modules/

%build
cd $RPM_BUILD_DIR/webcounter-%{version}/apache_%{apver}
LD_SHLIB="ld"
LDFLAGS_SHLIB="-G"
LD_LIBRARY_PATH=/usr/local/lib
LD_RUN_PATH=/usr/local/lib
export LD_SHLIB LD_LIBRARY_PATH
export LDFLAGS_SHLIB LD_RUN_PATH

./configure --activate-module=src/modules/cntr/libcntr.so
cd src/modules/cntr
make

%install
mkdir -p /var/tmp/%{name}-root/usr/local/apache-%{apver}/libexec/
cp $RPM_BUILD_DIR/webcounter-%{version}/apache_%{apver}/src/modules/cntr/libcntr.so /var/tmp/%{name}-root/usr/local/apache-%{apver}/libexec/
cd ..

mkdir -p /var/tmp/%{name}-root/usr/local/apache-%{apver}/htdocs/webcounter
cd $RPM_BUILD_DIR/webcounter-%{version}
cp -r digits count.cgi show-digits.cgi /var/tmp/%{name}-root/usr/local/apache-%{apver}/htdocs/webcounter

mkdir -p /var/tmp/%{name}-root/usr/local/bin
cp *pl /var/tmp/%{name}-root/usr/local/bin

%post
cat << EOF 
Run '%{apache_prefix}/bin/apxs -aen "cntr" %{apache_prefix}/libexec/libcntr.so' to set up webcounter.
You will also need to add something like this to httpd.conf:

 <IfModule libcntr.a>
 CounterAutoAdd    On
 CounterFile       logs/%v
 CounterTimeFmt   "%A, %d-%b-%y %T %Z"
 CounterFaceDir   /usr/local/apache-1.3.23/htdocs/webcounter/digits
 </IfModule>

 <Location /server-cntr>
 SetHandler server-cntr
 </Location>

 <Location /server-cntr-debug>
 SetHandler server-cntr-debug
 </Location>

More information is available at: http://www.dan.co.jp/webcounter/
EOF

%files
%defattr(-,root,other)
%doc index.html
/usr/local/apache-%{apver}/libexec/*cntr*
/usr/local/apache-%{apver}/htdocs/webcounter
/usr/local/bin/countctl.pl
/usr/local/bin/renamegif.pl
