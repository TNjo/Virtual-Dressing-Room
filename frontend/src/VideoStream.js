import React, { Component } from 'react';
import axios from 'axios';
import './css/style.css';
import img from './img/1.jpg';
class VideoStream extends Component {
  state = {
    response: '',
  };

  handleRunScript = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:5000/run_script');
      this.setState({ response: response.data });
    } catch (error) {
      console.error('Error:', error);
    }
  };

  handleStopScript = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:5000/terminate');
      this.setState({ response: response.data });
    } catch (error) {
      console.error('Error:', error);
    }
  };

 

  render() {
    return (
      // <div className="App">
      //   <h1>React + Python Communication</h1>
      //   <button onClick={this.handleRunScript}>Run Script</button>
      //   <div>
      //     <strong>Response:</strong> {this.state.response}
      //   </div>

      // </div>

      <div className="App">
        
    <header class="container header">
      
      <nav class="nav">
        <div class="logo">
          <h2>TryOn..</h2>
        </div>

        <div class="nav_menu" id="nav_menu">
          <button class="close_btn" id="close_btn">
            <i class="ri-close-fill"></i>
          </button>

          <ul class="nav_menu_list">
            <li class="nav_menu_item">
              <a href="#" class="nav_menu_link">account</a>
            </li>
            <li class="nav_menu_item">
              <a href="#" class="nav_menu_link">about</a>
            </li>
            <li class="nav_menu_item">
              <a href="#" class="nav_menu_link">service</a>
            </li>
            <li class="nav_menu_item">
              <a href="#" class="nav_menu_link">contact</a>
            </li>
          </ul>
        </div>

        <button class="toggle_btn" id="toggle_btn">
          <i class="ri-menu-line"></i>
        </button>
      </nav>
    </header>

    <section class="wrapper">
      <div class="container">
        <div class="grid-cols-2">
          <div class="grid-item-1">
            <h1 class="main-heading">
              Welcome to <span>TryOn.</span>
              <br />
              Virtual Dressing Room.
            </h1>
            <p class="info-text">
            Revolutionize Your Shopping Experience:
             Say Goodbye to Fitting Rooms! Try on Clothes in Real-Time.
            </p>

            <div class="btn_wrapper">
              <button class="btn view_more_btn" onClick={this.handleRunScript}>
                Let's Try On <i class="ri-arrow-right-line"></i>
              </button>

              <button class="btn documentation_btn"onClick={this.handleStopScript}>Stop</button>
            </div>
          </div>
          <div class="grid-item-2">
            <div class="team_img_wrapper">
              <img src={img} alt="team-img" />
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="wrapper">
      <div class="container" data-aos="fade-up" data-aos-duration="1000">
        <div class="grid-cols-3">
          <div class="grid-col-item">
            <div class="icon">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"
                />
              </svg>
            </div>
            <div class="featured_info">
              <span>Customize Your Clothes </span>
              <p>
              Elevate your fashion game with our innovative platform. Unleash your 
              creativity by customizing clothes to reflect your unique style,
              making every outfit uniquely yours.
              </p>
            </div>
          </div>
          <div class="grid-col-item">
            <div class="icon">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M17 14v6m-3-3h6M6 10h2a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v2a2 2 0 002 2zm10 0h2a2 2 0 002-2V6a2 2 0 00-2-2h-2a2 2 0 00-2 2v2a2 2 0 002 2zM6 20h2a2 2 0 002-2v-2a2 2 0 00-2-2H6a2 2 0 00-2 2v2a2 2 0 002 2z"
                />
              </svg>
            </div>
            <div class="featured_info">
              <span>Get recommendations</span>
              <p>
              Experience fashion like never before with personalized recommendations. Our platform takes your skin tone and style choices into account, ensuring outfits that perfectly suit your unique taste
              </p>
            </div>
          </div>

          <div class="grid-col-item">
            <div class="icon">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M.5 1a.5.5 0 0 0 0 1h1.11l.401 1.607 1.498 7.985A.5.5 0 0 0 4 12h1a2 2 0 1 0 0 4 2 2 0 0 0 0-4h7a2 2 0 1 0 0 4 2 2 0 0 0 0-4h1a.5.5 0 0 0 .491-.408l1.5-8A.5.5 0 0 0 14.5 3H2.89l-.405-1.621A.5.5 0 0 0 2 1H.5zM6 14a1 1 0 1 1-2 0 1 1 0 0 1 2 0zm7 0a1 1 0 1 1-2 0 1 1 0 0 1 2 0zm-1.646-7.646-3 3a.5.5 0 0 1-.708 0l-1.5-1.5a.5.5 0 1 1 .708-.708L8 8.293l2.646-2.647a.5.5 0 0 1 .708.708z"
                />
              </svg>
            </div>
            <div class="featured_info">
              <span>Place Order</span>
              <p>
              Browse, order, and enjoy hassle-free doorstep delivery of your favorite clothes. Elevate your shopping experience with convenient and stylish deliveries.
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <footer></footer>
      </div>

     

    );
  }
}

export default VideoStream;
