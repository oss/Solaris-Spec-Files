Summary: JWChat - Jabber Web Chat
Name: jwchat
Version: 0.9
Release: 1
License: GPL
Group: Applications/Internet
Source: %{name}-%{version}.tar.gz
URL: http://jwchat.sourceforge.net
BuildRoot: /var/tmp/%{name}-root
Requires: apache, perl, perl-module-Locale-Maketext, perl-module-Locale-Maketext-Fuzzy, perl-module-Locale-Maketext-Lexicon, perl-module-Regexp-Common, perl-module-Encode-compat, perl-module-Text-Iconv
BuildRequires: perl, perl-module-Locale-Maketext, perl-module-Locale-Maketext-Fuzzy, perl-module-Locale-Maketext-Lexicon, perl-module-Regexp-Common, perl-module-Encode-compat, perl-module-Text-Iconv

%description
JWChat aims to be a full featured, web based jabber client. It uses
only JavaScript and HTML on the client-side. Currently it supports
basic jabber instant messaging, roster management and muc-based
groupchats.

%prep
%setup -q

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
rm -rf %{buildroot}/usr/local/jwchat
mkdir -p %{buildroot}/usr/local/jwchat
mv htdocs %{buildroot}/usr/local/jwchat

%files
%defattr(-, root, root)
/usr/local/jwchat
