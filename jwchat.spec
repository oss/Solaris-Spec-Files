Summary: JWChat - Jabber Web Chat
Name: jwchat
Version: 0.9
%define jsjacname jsjac
Release: 3
License: GPL
Group: Applications/Internet
Source: %{name}-%{version}.tar.gz
Source1: %{jsjacname}.tar.gz
URL: http://jwchat.sourceforge.net
BuildRoot: /var/tmp/%{name}-root
# Are these actually 'Requires' or just 'BuildRequires'?
Requires: apache
BuildRequires: perl, perl-module-Locale-Maketext, perl-module-Locale-Maketext-Fuzzy, perl-module-Locale-Maketext-Lexicon, perl-module-Regexp-Common, perl-module-Encode-compat, perl-module-Text-Iconv

%description
JWChat aims to be a full featured, web based jabber client. It uses
only JavaScript and HTML on the client-side. Currently it supports
basic jabber instant messaging, roster management and muc-based
groupchats.

%prep
%setup -q
%setup -q -D -T -a 1 -n %{name}-%{version}

%build
# When we get perl 5.8.1 this sed stuff shouldn't be necessary anymore.
sed 's/binmode/#binmode/' scripts/templateparser.pl > scripts/templateparser.sed
mv scripts/templateparser.pl scripts/templateparser.bak
mv scripts/templateparser.sed scripts/templateparser.pl
chmod 755 scripts/templateparser.pl

sed 's/-e/-d/' Makefile > Makefile.sed
mv Makefile Makefile.bak
mv Makefile.sed Makefile

make

%install
mv jsjac/*.js htdocs
rm -rf %{buildroot}/usr/local/jwchat
mkdir -p %{buildroot}/usr/local/jwchat
mv htdocs %{buildroot}/usr/local/jwchat

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
/usr/local/jwchat
