%include machine-header.spec

Summary: C interpreter
Name: EiC
Version: 4.3.0
Release: 1
License: Artistic
Group: Development/Languages
URL: http://www.kd-dev.com/~eic/
Source: %{name}src_%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: teTeX make

%description
EiC is a freely available C language interpreter in both source and
binary form. EiC allows you to write C programs, and then "execute"
them as if they were a script (like a Perl script or a shell
script). You can even embed EiC in your own programs, allowing your
application to have a "scripting" language that is syntactically
equivalent to C. It is also possible to let an EiC "script" call
compiled library code and for compiled code to make callbacks to EiC
user defined functions.

  [from the website]

%prep
%setup -q -n EiC

%build
if [ "X$PWD" != X`pwd` ]; then
    PWD=`pwd`
    export PWD
fi 
config/makeconfig
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/EiC/include %{buildroot}/usr/local/EiC/lib \
         %{buildroot}/usr/local/EiC/module %{buildroot}/usr/local/bin
gmake INSTALL_DIR=%{buildroot}/usr/local/bin

%install
umask 022
mkdir -p %{buildroot}/usr/local/EiC/include %{buildroot}/usr/local/EiC/lib \
         %{buildroot}/usr/local/EiC/module %{buildroot}/usr/local/bin

# Unfortunately this only installs the binary:
gmake install INSTALL_DIR=%{buildroot}/usr/local/bin

for DIR in include module lib; do
    cp -pr $DIR %{buildroot}/usr/local/EiC/$DIR
done

cd doc
PATH="/usr/local/teTeX/bin/%{sparc_arch}:$PATH" gmake EiC.dvi

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, bin)
%doc doc/EiC.ps README* LICENCE Distribution.txt *html Maintenance
/usr/local/EiC
/usr/local/bin/*
