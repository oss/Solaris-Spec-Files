%define apver 1.3.29
Summary: Makes including headers/footers easy
Name: apache-module-mod_layout
Version: 3.2
Release: 1
Group: Applications/Internet
License: BSD
Source: mod_layout-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root

%define apache_prefix /usr/local/apache-%{apver}

BuildRequires: apache apache-devel
Requires: apache

%description
mod_layout is an Apache module that provides both a Footer and Header 
directive to automagically include output from other URIs at the beginning 
and ending of a Web page. It can be used to wrap documents for a standard 
look and feel for a site (or to insert banners on any given document in a 
site). Currently known to support mod_perl, PHP and Apache JServ. Should 
support just about any type of handler.

%prep
%setup -q -n mod_layout-%{version}


%build
PATH="%{apache_prefix}/bin/:$PATH" make

%install
mkdir -p %{buildroot}/usr/local/apache-modules/
cp mod_layout.so %{buildroot}/usr/local/apache-modules/

%post
echo "Run 'apxs -aen \"layout\" /usr/local/apache-modules/mod_layout.so' to set up mod_layout."

%files
%defattr(-,root,other)
%doc faq.html README
/usr/local/apache-modules/mod_layout.so




