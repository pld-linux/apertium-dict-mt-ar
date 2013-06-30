Summary:	Maltese-Arabic language pair for Apertium
Summary(pl.UTF-8):	Para języków maltański-arabski dla Apertium
%define	lpair	mt-ar
Name:		apertium-dict-%{lpair}
Version:	0.1.0
Release:	1
License:	GPL v2+
Group:		Applications/Text
Source0:	http://downloads.sourceforge.net/apertium/apertium-%{lpair}-%{version}.tar.gz
# Source0-md5:	03c56fc959ff9a909f2c63e7da22dd75
URL:		http://www.apertium.org/
BuildRequires:	apertium-devel >= 3.2.0
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	libxslt-progs
BuildRequires:	lttoolbox >= 3.2.0
BuildRequires:	pkgconfig
BuildRequires:	vislcg3
Requires:	apertium >= 3.2.0
Requires:	lttoolbox >= 3.2.0
Requires:	vislcg3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an Apertium language pair, which can be used for translating
between Maltese and Arabic, morphological analysis or part-of-speech
tagging of both languages.

%description -l pl.UTF-8
Ten pakiet zawiera parę języków dla Apertium służącą do tłumaczenia
między maltańskim a arabskim, a także analizy morfologicznej lub
oznaczania części mowy w obu językach.

%prep
%setup -q -n apertium-%{lpair}-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%{_datadir}/apertium/apertium-%{lpair}
%{_datadir}/apertium/modes/ar-mt.mode
%{_datadir}/apertium/modes/mt-ar.mode
