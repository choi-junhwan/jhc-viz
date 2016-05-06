from flask import Flask, render_template, request, redirect
import counts_by_hour
import map_static
import map_live

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/bus_count')
def bus_count():
    script, div = counts_by_hour.plot_count_by_hour()
    return render_template('bus_count.html', script=script, div=div)


@app.route('/bus_static')
def bus_static():
    nyc = map_static.read_bus_loc()
    data = nyc[['latitude','longitude']].values.tolist()
    return render_template('bus_static.html', data=data)

@app.route('/bus_live')
def bus_live():
    nyc = map_live.nyc_current()
    """
    plotdf = nyc[['MonitoredVehicleJourney_PublishedLineName',
                  'MonitoredVehicleJourney_VehicleLocation_Latitude',
                  'MonitoredVehicleJourney_VehicleLocation_Longitude']]
    """
    data = nyc[['MonitoredVehicleJourney_VehicleLocation_Latitude',
                'MonitoredVehicleJourney_VehicleLocation_Longitude']].values.tolist()
    return render_template('bus_live.html', data=data)

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0')
