MODULE_TOPDIR = ..

SUBDIRS = \
	r.basins.fill \
	r.buffer \
	r.buildvrt \
	r.carve \
	r.category \
	r.circle \
	r.clump \
	r.coin \
	r.colors \
	r.colors.out \
	r.composite \
	r.compress \
	r.contour \
	r.cost \
	r.covar \
	r.cross \
	r.describe \
	r.distance \
	r.external \
	r.external.out \
	r.fill.dir \
	r.fill.stats \
	r.flow \
	r.geomorphon \
	r.grow.distance \
	r.gwflow \
	r.his \
	r.horizon \
	r.in.ascii \
	r.in.bin \
	r.in.gdal \
	r.in.gridatb \
	r.in.lidar \
	r.in.mat \
	r.in.pdal \
	r.in.png \
	r.in.poly \
	r.in.xyz \
	r.info \
	r.kappa \
	r.latlong \
	r.lake \
	r.li \
	r.mapcalc \
	r.mask.status \
	r.mfilter \
	r.mode \
	r.neighbors \
	r.null \
	r.object.geometry \
	r.out.ascii \
	r.out.bin \
	r.out.gdal \
	r.out.gridatb \
	r.out.mat \
	r.out.mpeg \
	r.out.png \
	r.out.pov \
	r.out.ppm \
	r.out.ppm3 \
	r.out.vrml \
	r.out.vtk \
	r.param.scale \
	r.patch \
	r.path \
	r.profile \
	r.proj \
	r.quant \
	r.quantile \
	r.random \
	r.random.cells \
	r.random.surface \
	r.reclass \
	r.recode \
	r.region \
	r.regression.line \
	r.regression.multi \
	r.report \
	r.resamp.bspline \
	r.resamp.filter \
	r.resamp.interp \
	r.resamp.rst \
	r.resamp.stats \
	r.resample \
	r.rescale \
	r.rescale.eq \
	r.ros \
	r.series \
	r.series.accumulate \
	r.series.interp \
	r.relief \
	r.sim \
	r.slope.aspect \
	r.smooth.edgepreserve \
	r.solute.transport \
	r.spread \
	r.spreadpath \
	r.statistics \
	r.stats.zonal \
	r.stats.quantile \
	r.stats \
	r.stream.extract \
	r.sun \
	r.sunhours \
	r.sunmask \
	r.support \
	r.support.stats \
	r.surf.area \
	r.surf.contour \
	r.surf.fractal \
	r.surf.gauss \
	r.surf.idw \
	r.surf.random \
	r.terraflow \
	r.texture \
	r.thin \
	r.tile \
	r.timestamp \
	r.to.rast3 \
	r.to.rast3elev \
	r.to.vect \
	r.topidx \
	r.topmodel \
	r.transect \
	r.univar \
	r.uslek \
	r.usler \
	r.viewshed \
	r.volume \
	r.walk \
	r.water.outlet \
	r.watershed \
	r.what \
	r.what.color

PGM = rasterintro

include $(MODULE_TOPDIR)/include/Make/Dir.make

default:
	$(MAKE) htmldir

htmldir: parsubdirs

$(HTMLDIR)/r.in.png:
	# no-op - override Html.make rule for .png image files
$(MDDIR)/source/r.in.png:
	# no-op - override Html.make rule for .png image files

$(HTMLDIR)/r.out.png:
	# no-op - override Html.make rule for .png image files
$(MDDIR)/source/r.out.png:
	# no-op - override Html.make rule for .png image files

r.colors: r.mapcalc
