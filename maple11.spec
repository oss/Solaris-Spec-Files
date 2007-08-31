%define __find_requires %{nil}
%define __find_provides %{nil}

Name: maple
Summary: Maple 11
Version: 11
Release: 2
Group: Licensed
Copyright: Licensed
Source0: maple%{version}.tar.gz
Source1: maple.README.rutgers
Source2: maple.init.d
# To build the maple11.tar.gz, go through the GUI maple installer and install
# maple and the network tools into /usr/local/maple11/{maple11,Network...}
# then run tar cf maple11.tar maple11 in /usr/local
BuildRoot: /var/tmp/%{name}-root

%description
Maple 11 is an essential tool for researchers, teachers, and students in any
technical discipline. It lets you explore, visualize, and solve even the most
complex mathematical problems, providing greater insight into the math and
reducing errors. Teachers can bring both simple and complex problems to life;
students can focus on concepts rather than the mechanics of solutions; and
researchers can develop more sophisticated algorithms or models.


%prep
%setup -q -n maple%{version}

%build
echo "Nothing to do"  # Nothing to do

%install
mkdir -p $RPM_BUILD_ROOT/usr/local/maple11
mkdir -p $RPM_BUILD_ROOT/etc/init.d

# Copy the stuff to the build root
cp -r maple11 Maple_Network_Tools $RPM_BUILD_ROOT/usr/local/maple11
cp %{SOURCE1} $RPM_BUILD_ROOT/usr/local/maple11/README.rutgers
cp %{SOURCE2} $RPM_BUILD_ROOT/etc/init.d/maple

cd $RPM_BUILD_ROOT/usr/local
ln -s maple11 maple

%post
cat <<EOF
 
====================================================================
 You might want to make a /etc/rc2.d/maple link, to start the maple
 license server at boot time
 ln -s /etc/init.d/maple /etc/rc2.d/S99maple

 Read the README.rutgers for more hints on setting this software up
 for use at Rutgers.  This file is located in /usr/local/maple11.
====================================================================

EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%dir /usr/local/maple11
/usr/local/maple11/*
/usr/local/maple
%attr(755,root,root)/etc/init.d/maple

