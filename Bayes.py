#!/usr/bin/env python
# coding: utf-8

# In[8]:


# probabilidades de la condiciones de los sintomas dado COVID 19
p_fatiga_given_covid=0.9
p_tos_seca_given_covid=0.7
p_dificultad_respirar_given_covid=0.6
p_dolor_garganta_given_covid=0.5
p_dolor_cabeza_given_covid=0.6
p_dolor_cuerpo_given_covid=0.5
p_escalofrios_given_covid=0.4
p_secrecion_nasal_given_covid=0.2
p_perdida_sentido_given_covid=0.5
p_fiebre_given_covid=0.8
p_dolor_pecho_given_covid=0.3

#definir prevalencia de covid en la poblacion
p_covid=0.05
#sintomas observados en el paciente
sintomas=["Fatiga","Tos seca","Dificultad para respirar","Dolor de garganta",
          "Dolor de cabeza","Dolor en le cuerpo","Escalofrios","Secrecion nasal",
          "Perdida de sentido del olfato o del gusto","Fiebre","Dolor de pecho"]
#Calcular la probabilidad de que el paciente tenga COVID 19
p_sintomas_given_covid= p_fatiga_given_covid*p_tos_seca_given_covid*p_dificultad_respirar_given_covid*\
                        p_dolor_garganta_given_covid*p_dolor_cabeza_given_covid*p_dolor_cuerpo_given_covid*\
                        p_escalofrios_given_covid*p_secrecion_nasal_given_covid*p_perdida_sentido_given_covid*\
                        p_fiebre_given_covid*p_dolor_pecho_given_covid
            
p_sintomas_given_no_covid=0.05**11 #la probabilidad de tener estos sintomas sin covid es muy bajo
p_sintomas=p_sintomas_given_covid*p_covid+p_sintomas_given_no_covid*(1-p_covid)
p_covid_given_sintomas=p_sintomas_given_covid*p_covid/p_sintomas
print(f"la probabilidad de que el paciente tenga COVID-19 dado los sintomas es: {p_covid_given_sintomas}")


# In[ ]:




