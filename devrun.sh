export FLASK_ENV=development
export FLASK_APP=gravelfinder.py
echo "Google API Key used is [$GOOGLE_API_KEY]"

if [ "x$GOOGLE_API_KEY" = "x" ]; then
    echo "SET the GOOGLE_API_KEY environment variable!"
    echo "QUIT!"
    exit 1
fi

./geojson.py
flask run --host=0.0.0.0 --port 8080
