from django.views.generic import View
from bims.models.biotope import Biotope
from bims.models.sampling_method import SamplingMethod
from bims.models.biological_collection_record import BiologicalCollectionRecord
from bims.models.site_image import SiteImage
from bims.enums.taxonomic_group_category import TaxonomicGroupCategory


class SiteVisitBaseView(View):
    object = None

    def taxon_group(self):
        """Get taxon group for the current site visit"""
        if self.collection_records.exists():
            return self.collection_records[0].taxonomy.taxongroup_set.filter(
                category=TaxonomicGroupCategory.SPECIES_MODULE.name
            )[0]
        return None

    def owner(self):
        """Get owner of the site visit"""
        if self.object.owner:
            return self.object.owner
        if self.collection_records.exists():
            return self.collection_records[0].owner
        return None

    def collector(self):
        """Get the collector of the site visit"""
        if self.object.collector_user:
            return self.object.collector_user
        collector_from_collection = (
            self.collection_records.filter(collector_user__isnull=False)
        )
        if collector_from_collection.exists():
            return collector_from_collection[0].collector_user
        return None

    def biotope(self, biotope_type):
        """Get a biotope from collection records"""
        biotope = self.collection_records.values(biotope_type)
        if biotope:
            try:
                return Biotope.objects.filter(id__in=biotope)[0]
            except IndexError:
                return None
        return None

    def sampling_method(self):
        """Get existing sampling method value from collections"""
        sampling_method = self.collection_records.values(
            'sampling_method'
        )
        if sampling_method:
            try:
                return SamplingMethod.objects.filter(
                    id__in=sampling_method
                )[0]
            except IndexError:
                return None
        return None

    def sampling_effort(self):
        """Get existing sampling effort value from collections"""
        sampling_effort = self.collection_records.exclude(
            sampling_effort=''
        )
        try:
            if sampling_effort.exists():
                sampling_effort_str = sampling_effort[0].sampling_effort
                sampling_effort_arr = sampling_effort_str.split(' ')
                return (
                    sampling_effort_arr[0].strip(),
                    sampling_effort_arr[1].strip()
                )
        except IndexError:
            pass
        return '', ''

    def abundance_type(self):
        """Get existing abundance type from collection"""
        abundance_type = self.collection_records.exclude(
            abundance_type=''
        )
        if abundance_type.exists():
            return abundance_type[0].abundance_type
        return None

    def source_reference(self):
        """Get existing source reference"""
        source_reference_records = self.collection_records.exclude(
            source_reference__isnull=True
        )
        if source_reference_records.exists():
            return source_reference_records[0].source_reference
        return None

    def get_context_data(self, **kwargs):
        context = super(SiteVisitBaseView, self).get_context_data(**kwargs)
        self.collection_records = (
            BiologicalCollectionRecord.objects.filter(
                survey=self.object.id
            ).order_by('taxonomy__canonical_name')
        )
        context['source_reference'] = self.source_reference()
        context['collection_records'] = self.collection_records
        context['taxon_group'] = self.taxon_group()
        context['owner'] = self.owner()
        context['collector'] = self.collector()
        context['biotope'] = self.biotope('biotope')
        context['specific_biotope'] = self.biotope('specific_biotope')
        context['substratum'] = self.biotope('substratum')
        context['sampling_method'] = self.sampling_method()
        sampling_effort_value, sampling_effort_unit = self.sampling_effort()
        context['sampling_effort_value'] = sampling_effort_value
        context['sampling_effort_unit'] = sampling_effort_unit
        context['abundance_type'] = self.abundance_type()

        context['broad_biotope_list'] = (
            Biotope.objects.broad_biotope_list(
                taxon_group=context['taxon_group']
            )
        )
        context['specific_biotope_list'] = (
            Biotope.objects.specific_biotope_list(
                taxon_group=context['taxon_group']
            )
        )
        context['substratum_list'] = (
            Biotope.objects.substratum_list(
                taxon_group=context['taxon_group']
            )
        )
        context['sampling_method_list'] = (
            SamplingMethod.objects.sampling_method_list(
                taxon_group=context['taxon_group']
            )
        )
        try:
            context['site_image'] = SiteImage.objects.get(
                survey=self.object
            )
        except SiteImage.DoesNotExist:
            pass
        return context
