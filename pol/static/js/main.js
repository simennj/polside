window.onpopstate = function (event) {
    if (event.state == null) {
        $('.filterform').find('input').val('');
        $('.selectpicker').selectpicker('deselectAll');
        loadTable(true);
    } else {
        console.log(event.state);
        var values = {};
        var varetyper = [];
        $.each(event.state, function (i, field) {
            if (field.name == 'varetype') {
                varetyper.push(field.value);
            } else {
                values[field.name] = field.value;
            }
        });
        $('.selectpicker').selectpicker('val', varetyper);
        $('.filterform').find('input').val(function () {
            return values[this.name];
        });
        $('#id_o').val(values['o']);
        loadTable(true);
    }
};

var ffselector = $('.filterform');
var filterform = ffselector.serialize();

$(document).ready(function () {
    loadTable(true); // TODO: sometimes load twice
    $('.filterform').change(loadTable);
});

function loadTable(nopush) {
    filterform = ffselector.find(':input').filter(function () {
        return $.trim(this.value).length > 0;
    }).serialize();
    if (nopush != true) {
        history.pushState(ffselector.serializeArray(), 'asdf', '/?' + filterform);
    }
    $.ajax({
        type: 'GET',
        url: '/table',
        data: filterform,
        success: function (data) {
            $('#table').html(data);
            $('.tablesort span').removeClass();
            var sortedby = $('#id_o')[0].selectedIndex;
            var desc = sortedby % 2;
            if (desc) {
                $('#o_' + (sortedby - desc)).addClass('fa fa-sort-desc');
            } else {
                $('#o_' + (sortedby)).addClass('fa fa-sort-asc');
            }
        }
    });
}

var sistvarenummer;
function utvid(varenummer) {
    var sistvare = $('#' + sistvarenummer);
    if (sistvarenummer > 0) {
        sistvare.slideUp();
    }
    if (varenummer == sistvarenummer) {
        sistvarenummer = 0;
        return sistvarenummer;
    }
    sistvarenummer = varenummer;
    var vare = $('#' + varenummer);
    $.ajax({
        type: 'GET',
        url: '/produkt/' + varenummer,
        success: function (data) {
            vare.html(data).slideDown();
        }
    });
}

function sort(query) {
    var valgtselector = $('#id_o').find('option');
    var valgt = valgtselector.eq(query);
    if (valgt.is(':selected'))
        valgtselector.eq(query + 1).prop('selected', true);
    else
        valgt.prop('selected', true);
    loadTable();
}

function page(number) {
    $('#side').val(number);
    loadTable();
    return false
}

function paginationNavigation(current, total) {
    var active = current;
    var count = total;
    var start = 0;
    var end = 12;
    $('#sidenummer_' + active).addClass('active');
    if (count > 12) {
        if (active > 6) {
            end = Math.min(active + 6, count);
            start = Math.max(active - 6, 0);
        }
        if (count - active < 6) {
            start = count - 12;
        }
        $('.sidenummer').hide().slice(start, end).show();
    }
}
function lastKart() {
    if ($('#kart').html().length == 0) {
        var options = {
            infowindow: false
        };
        cartodb.createVis('kart', 'https://simennj.cartodb.com/api/v2/viz/16b23eda-69d2-11e5-a1bb-0e674067d321/viz.json', options)
            .done(function (vis, layers) {
                //layers[1].setInteraction(true);
                layers[1].setInteractivity("butikknavn, kategori");
                layers[1].on('featureClick', function (e, latlng, pos, data) {
                    $('#id_butikkategori').val(data.kategori);
                    loadTable();
                    $('#kartholder').collapse('hide');
                });
            });
    }
}