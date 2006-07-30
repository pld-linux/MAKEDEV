Summary:	Program to make and update /dev entries
Summary(de):	Script zum Erstellen und Aktualisieren von /dev-Einträgen
Summary(es):	Script para hacer y actualizar entradas referentes a dispositivos en /dev
Summary(fr):	Script pour créer et mettre à jour les entrées /dev
Summary(pl):	Program do tworzenia i poprawiania urz±dzeñ z /dev
Summary(pt_BR):	Script para fazer e atualizar entradas referentes a dispositivos em /dev
Summary(tr):	Aygýt tanýmý yapmak ve deðiþtirmek için bir araç
Name:		MAKEDEV
Version:	3.13
Release:	2
License:	GPL v2+
Group:		Applications/System
Source0:	%{name}-%{version}-1.tar.gz
# Source0-md5:	f8befaebd0813c6fa59c07ef3875f232
Patch0:		%{name}-ub.patch
BuildRequires:	libselinux-devel >= 0:1.8
Requires:	libselinux >= 0:1.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_bindir		/sbin

%description
The /dev tree holds special files, each of which corresponds to a type
of hardware device that Linux supports. This package contains a
program which makes it easier to create and maintain the files which
fill the /dev tree.

%description -l de
Die /dev-Hierarchie enthält spezielle Dateien, von denen jede einem
Hardwaregerättyp entspricht, der von Linux unterstützt wird. Dieses
Paket enthält ein Skript, das die Erstellung und die Pflege der
Dateien innerhalb dieser Hierarchie vereinfacht.

%description -l es
El directorio /dev posee archivos especiales, cada uno de ellos
correspondiendo a un tipo de dispositivo de hardware que Linux
soporta. Este paquete contiene un script que hace más fácil la
creación y manutención de los archivos en el directorio /dev.

%description -l fr
L'arborescence /dev contient des fichiers spéciaux. Chacun d'eux
correspond à un périphérique matériel gérable par Linux. Ce paquetage
contient un script facilitant la création et la maintenance des
fichiers qui remplissent l'arborescence /dev.

%description -l pl
Pliki specjalne znajduj±ce siê w katalogu /dev odpowiadaj±
urz±dzeniom, które s± obs³ugiwane przez Linuksa. Pakiet ten zawiera
program, który uczyni tworzenie i operowanie tymi plikami ³atwiejszym.

%description -l pt_BR
O diretório /dev possui arquivos especiais, cada um deles
correspondendo a um tipo de dispositivo de hardware que o Linux
suporta. Este pacote contém um script que torna mais fácil a criação
e manutenção dos arquivos no diretório /dev.

%description -l tr
Unix ve Unix benzeri sistemler (Linux da dahil olmak üzere), makinaya
baðlý aygýtlarý göstermek için özel dosyalar kullanýrlar. Bu özel
dosyalarýn tümü /dev dizin yapýsý altýndadýr. Bu paket en çok
kullanýlan /dev dosyalarýný içerir. Bu dosyalar, bir sistemin düzgün
olarak iþleyebilmesi için temel gereksinimlerdendir.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	OPTFLAGS="%{rpmcflags} %{rpmldflags}" \
	SELINUX=1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man8}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	devdir=/dev \
	makedevdir=/sbin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/MAKEDEV
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
%config %{_sysconfdir}/makedev.d
