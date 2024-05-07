import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# User inputs
st.subheader("User Inputs")
L = st.number_input("Length of the structure (m)", value=100.0)
c = st.number_input("Wave speed (m/s)", value=1.0)
k = st.number_input("Stiffness (N/m)", value=1.0)
m = st.number_input("Mass (kg)", value=1.0)
omega = 2 * np.pi * st.number_input("Frequency of the wave (Hz)", value=5.0)
t = np.linspace(0, st.number_input("Time (s)", value=20.0), 1000)
damping_ratio = st.number_input("Damping ratio", value=0.1)

# One-dimensional wave equation
def wave_eqn(y, t):
    if damping_ratio == 0:
        dydt = [y[1], -k/m * y[0]]
    else:
        dydt = [y[1], -k/m * y[0] + c/m * y[1]]
    return dydt


# Initial conditions
y0 = [0, 1]  # Initial displacement and velocity

# Solve ODE
sol = odeint(wave_eqn, y0, t)

# Isolation technique (damping)
decay_factor = np.exp(-damping_ratio * omega * t)
damped_sol = sol.copy()
damped_sol[:, 0] *= decay_factor  # Apply decay factor to displacement
damped_sol[:, 1] *= decay_factor  # Apply decay factor to velocity

# Streamlit UI
st.title("Advanced Earthquake Wave Propagation and Isolation Demonstration")

# Plotting
st.subheader("Wave Propagation")
plt.plot(t, sol[:, 0], label='Displacement')
plt.plot(t, sol[:, 1], label='Velocity')
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
st.pyplot(plt.gcf())

# Explanation of how wave speed affects the graph
st.subheader("Effect of Wave Speed on Amplitude vs Time Graph")
st.write("The wave speed (c) affects how quickly the seismic waves travel through the structure. Increasing the wave speed will lead to more rapid vibrations and potentially more damage to the structure. This can be observed in the graph as an increase in the frequency of the waves.")

# Explanation of how stiffness affects the graph
st.subheader("Effect of Stiffness on Amplitude vs Time Graph")
st.write("The stiffness (k) of a structure determines how resistant it is to deformation. Increasing the stiffness will make the structure vibrate less when subjected to seismic waves. However, increasing the stiffness also increases the natural frequency of the structure, which can make it more susceptible to resonance with certain frequencies of seismic waves. This can be observed in the graph as an increase in the amplitude of the waves at certain frequencies.")

# Explanation of how damping affects the graph
st.subheader("Effect of Damping on Amplitude vs Time Graph")
st.write("Damping is a technique used to reduce the amplitude of vibrations in a structure. In the context of earthquake wave propagation, damping can be used to reduce the effects of seismic waves on the structure. The damping ratio determines how quickly the amplitude of the waves decays over time. Increasing the damping ratio will lead to a faster decay of the waves, which can be observed in the graph as a decrease in the amplitude of the waves over time.")

# Plotting with isolation
st.subheader("Wave Propagation with Isolation")
plt.plot(t, damped_sol[:, 0], label='Displacement')
plt.plot(t, damped_sol[:, 1], label='Velocity')
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
st.pyplot(plt.gcf())

# Explanation of how changing two properties at once affects the graph
st.subheader("Effect of Changing Two Properties at Once on Amplitude vs Time Graph")
st.write("Changing two properties at once can have complex effects on the amplitude vs time graph. For example, increasing both the wave speed and stiffness can lead to more rapid vibrations, but also increase the natural frequency of the structure, potentially leading to resonance. Increasing the damping ratio can help mitigate the effects of seismic waves, but may also reduce the overall response of the structure.")

# User input to demonstrate results
st.subheader("Demonstration")
st.write("Use the sliders above to adjust the wave speed, stiffness, damping ratio, and other properties to see how they affect the amplitude vs time graph.")
