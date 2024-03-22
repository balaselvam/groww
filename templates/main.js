$(document).ready(function() {
    function refreshTable() {
        $.getJSON('/api/table-data', function(data) {
            // Update the table with the new data
            var tableBody = '';
            var tableBody_next = '';
            var tableBody_far = '';
            var curr_time = '<h4 class="text-success">' + data.curr_time + '</h4>';
            $('#curr_time').html(curr_time);
            let tot_CE_oi = 0
            let tot_PE_oi = 0
            let tot_CE_oi_next = 0
            let tot_PE_oi_next = 0
            let tot_CE_oi_far = 0
            let tot_PE_oi_far = 0
            let tot_CE_vol = 0
            let tot_PE_vol = 0
            let tot_CE_vol_next = 0
            let tot_PE_vol_next = 0
            let tot_CE_vol_far = 0
            let tot_PE_vol_far = 0
            
            data.oi_data.forEach(dataRow => {
                var strikePrice = dataRow.strikePrice;
                var ce_openInterest = dataRow.ce_openInterest;
                var pe_openInterest = dataRow.pe_openInterest;
                var ce_volume = dataRow.ce_volume;
                var pe_volume = dataRow.pe_volume;
                tot_CE_oi +=  ce_openInterest;
                tot_PE_oi +=  pe_openInterest;
                tot_CE_vol += ce_volume;
                tot_PE_vol += pe_volume;
                tableBody += '<tr><td>' + (strikePrice)/100 + '</td><td>' + ce_openInterest + '</td><td>' + pe_openInterest + '</td><td>' + ce_volume + '</td><td>' + pe_volume + '</td></tr>';
            });
            data.oi_data_next.forEach(dataRow => {
                var strikePrice = dataRow.strikePrice;
                var ce_openInterest_next = dataRow.ce_openInterest;
                var pe_openInterest_next = dataRow.pe_openInterest;
                var ce_volume_next = dataRow.ce_volume;
                var pe_volume_next = dataRow.pe_volume;
                tot_CE_oi_next += ce_openInterest_next;
                tot_PE_oi_next += pe_openInterest_next;
                tot_CE_vol_next += ce_volume_next;
                tot_PE_vol_next += pe_volume_next;
                tableBody_next += '<tr><td>' + (strikePrice)/100 + '</td><td>' + ce_openInterest_next + '</td><td>' + pe_openInterest_next + '</td><td>' + ce_volume_next + '</td><td>' + pe_volume_next + '</td></tr>';
            });
            data.oi_data_far.forEach(dataRow => {
                var strikePrice = dataRow.strikePrice;
                var ce_openInterest_far = dataRow.ce_openInterest;
                var pe_openInterest_far = dataRow.pe_openInterest;
                var ce_volume_far = dataRow.ce_volume;
                var pe_volume_far = dataRow.pe_volume;
                tot_CE_oi_far += ce_openInterest_far;
                tot_PE_oi_far += pe_openInterest_far;
                tot_CE_vol_far += ce_volume_far;
                tot_PE_vol_far += pe_volume_far;
                tableBody_far += '<tr><td>' + (strikePrice)/100 + '</td><td>' + ce_openInterest_far + '</td><td>' + pe_openInterest_far + '</td><td>' + ce_volume_far + '</td><td>' + pe_volume_far + '</td></tr>';
            });
            var oi_PCR = tot_PE_oi/tot_CE_oi;
            var oi_PCR_next = tot_PE_oi_next/tot_CE_oi_next;
            var oi_PCR_far = tot_PE_oi_far/tot_CE_oi_far;
            var vol_PCR = tot_PE_vol/tot_CE_vol;
            var vol_PCR_next = tot_PE_vol_next/tot_CE_vol_next;
            var vol_PCR_far = tot_PE_vol_far/tot_CE_vol_far;

            if (oi_PCR != null && oi_PCR_next != null && oi_PCR_far != null) {
                var oi_PCR_avg = (oi_PCR+oi_PCR_next+oi_PCR_far)/3;
            }
            
            oi_PCR = oi_PCR.toFixed(5);
            oi_PCR_next = oi_PCR_next.toFixed(5);
            oi_PCR_far = oi_PCR_far.toFixed(5);
            oi_PCR_avg = oi_PCR_avg.toFixed(5);
            vol_PCR = vol_PCR.toFixed(5);
            vol_PCR_next = vol_PCR_next.toFixed(5);
            vol_PCR_far = vol_PCR_far.toFixed(5);
            $('#ce-oi').html(tot_CE_oi);
            $('#pe-oi').html(tot_PE_oi);
            $('#ce-oi-next').html(tot_CE_oi_next);
            $('#pe-oi-next').html(tot_PE_oi_next);
            $('#ce-oi-far').html(tot_CE_oi_far);
            $('#pe-oi-far').html(tot_PE_oi_far);
            $('#oi-pcr').html(oi_PCR);
            $('#oi-pcr-next').html(oi_PCR_next);
            $('#oi-pcr-far').html(oi_PCR_far);
            $('#oi-pcr-avg').html(oi_PCR_avg);
            $('#tot-ce-vol').html(tot_CE_vol);
            $('#tot-pe-vol').html(tot_PE_vol);
            $('#tot-ce-vol-next').html(tot_CE_vol_next);
            $('#tot-pe-vol-next').html(tot_PE_vol_next);
            $('#tot-ce-vol-far').html(tot_CE_vol_far);
            $('#tot-pe-vol-far').html(tot_PE_vol_far);
            $('#vol-pcr').html(vol_PCR);
            $('#vol-pcr-next').html(vol_PCR_next);
            $('#vol-pcr-far').html(vol_PCR_far);
            $('#table-body').html(tableBody);
            $('#table-body-next').html(tableBody_next);
            $('#table-body-far').html(tableBody_far);
        });
    }
    setInterval(refreshTable, 1000); // Refresh every second
});