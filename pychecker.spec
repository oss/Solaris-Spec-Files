%define python_ver 2.3.3

Summary: checks Python source code
Name: pychecker
Version: 0.8.13
Release: 2
Copyright: BSD
Group: Development/Tools
Source: http://easynews.dl.sourceforge.net/sourceforge/pychecker/pychecker-0.8.13.tar.gz
URL: http://pychecker.sourceforge.net
Packager: Robert Renaud <rrenaud@nbcs.rutgers.edu>
# might break with newer than 2.3, due to path issues
Requires: python = %{python_ver} 
BuildRequires: python = %{python_ver}
BuildRoot: %{_tmppath}/%{name}-root

%description
PyChecker is a tool for finding bugs in python source code. It finds problems 
that are typically caught by a compiler for less dynamic languages, like C 
and C++. It is similar to lint. Because of the dynamic nature of python, some 
warnings may be incorrect; however, spurious warnings should be fairly 
infrequent. 

%prep
%setup -q

%build
# empty

%install
python setup.py install --root=$RPM_BUILD_ROOT

%clean

%files 
%defattr(-,root,root)
%doc TODO VERSION README KNOWN_BUGS MAINTAINERS CHANGELOG COPYRIGHT
/usr/local/bin/pychecker
/usr/local/lib/python2.3/site-packages/pychecker/*



