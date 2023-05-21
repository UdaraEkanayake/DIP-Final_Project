from flask import Flask, request, render_template

damage_result = ...
repair_cost = ...

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        image = request.files['image']
        # Perform damage detection and assessment using the trained model
        # Estimate repair costs using the regression model
        # Display the results to the user
        return render_template('result.html', damage=damage_result, cost=repair_cost)
    return render_template('upload.html')

if __name__ == '__main__':
    app.run()

       
