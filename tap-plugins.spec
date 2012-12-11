%define name	tap-plugins
%define version 0.7.1
%define release %mkrel 1

Summary:      	Tom's Audio Processing plugins
Name:         	%{name}
Version:      	%{version}
Release:      	%{release}
License:    	GPL
Group:        	Sound
URL:          	http://tap-plugins.sourceforge.net/
Source0:      	tap-plugins-%{version}.tar.bz2
BuildRoot:    	%{_tmppath}/%{name}-buildroot

%description
TAP-plugins is short for Tom's Audio Processing plugins. It is a bunch
of LADSPA plugins for digital audio processing, intended for use in a
professional DAW environment such as Ardour.

%prep
%setup -q
perl -p -i -e "s/-O3/$RPM_OPT_FLAGS/g" Makefile

%build
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libdir}/ladspa
make INSTALL_PLUGINS_DIR=$RPM_BUILD_ROOT%{_libdir}/ladspa/ \
     INSTALL_LRDF_DIR=$RPM_BUILD_ROOT%{_datadir}/ladspa/rdf/ install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CREDITS README
%dir %{_libdir}/ladspa
%{_libdir}/ladspa/*.so
%{_datadir}/ladspa/rdf/*



%changelog
* Wed Mar 16 2011 Stéphane Téletchéa <steletch@mandriva.org> 0.7.1-1mdv2011.0
+ Revision: 645447
- update to new version 0.7.1

* Tue Sep 08 2009 Thierry Vignaud <tv@mandriva.org> 0.7.0-6mdv2010.0
+ Revision: 434274
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tv@mandriva.org> 0.7.0-5mdv2009.0
+ Revision: 261376
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 0.7.0-4mdv2009.0
+ Revision: 254121
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.7.0-2mdv2008.1
+ Revision: 128226
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import tap-plugins


* Wed Nov 9 2005 Austin Acton <austin@mandriva.org> 0.7.0-2mdk
- rebuild

* Fri Aug 20 2004 Austin Acton <austin@mandrake.org> 0.7.0-1mdk
- 0.7.0

* Tue Jun 22 2004 Austin Acton <austin@mandrake.org> 0.6.0-1mdk
- 0.6.0
- bzip source
- use proper cflags
- add docs

* Sat May 8 2004 Austin Acton <austin@mandrake.org> 0.4.0-1mdk
- steal from CCRMA

* Wed Feb 18 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.4.0-1
- do not depend on ladspa package explicitly
* Wed Feb  4 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.3.0-1
- updated to 0.3.0
* Thu Jan 29 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.0-1
- initial build
