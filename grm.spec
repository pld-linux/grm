%define		fversion	%(echo %{version} |tr . _)
Summary:	Grammar Library
Summary(pl):	Biblioteka gramatyk
Name:		grm
Version:	4.0
Release:	1
License:	Free for educational use, non-distributable
# from http://akpublic.research.att.com/cgi-bin/access.cgi/as/vt/ext-software/www-ne-license.cgi?form.grm.binary
Source0:	%{name}-%{fversion}.linux.i386.tar.gz
Group:		Applications/Text
URL:		http://www.research.att.com/sw/tools/grm/
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The GRM Library (Grammar Library) is a set of general-purpose software tools
for constructing, modifying, and compiling grammars. 

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man{1,3,5}}
install bin/* $RPM_BUILD_ROOT%{_bindir}
install doc/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
install doc/*.3 $RPM_BUILD_ROOT%{_mandir}/man3
install doc/*.5 $RPM_BUILD_ROOT%{_mandir}/man5

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
