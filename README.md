<div align="center">
  <img src="logo_blink.gif" alt="alt text" width="100"/>
</div>

<br/>

```java
public class GitHub {

    public static void main(String[] args) {
        GitHub GitHub = new GitHub();
        GitHub.exibirAboutMe();
        GitHub.exibirProjects();
        GitHub.exibirSkills();
        GitHub.exibirLinkedIn();
    }

    public void exibirAboutMe() {
        AboutMe AboutMe = new AboutMe();
        AboutMe.exibir();
    }

    public void exibirProjects() {
        Projects Projects = new Projects();
        Projects.exibir();
    }

    public void exibirSkills() {
        Skills Skills = new Skills();
        Skills.exibir();
    }

    public void exibirLinkedIn() {
        LinkedIn LinkedIn = new LinkedIn();
        LinkedIn.exibir();
    }
}

class AboutMe {
    public void exibir() {
        System.out.println("Sobre Mim");
        System.out.println("Experiência em Java para Android e backend com Java e Spring.");
        System.out.println("Graduado em Ciência da Computação e segunda graduação em Ciência de Dados e Machine Learning.");
        System.out.println("A combinação de desenvolvimento, estatística e aprendizado de máquina me empolgou.");
        System.out.println("Desde então, tenho me dedicado a essa área.");
        System.out.println("Ainda assim, de vez em quando, gosto de desenvolver algo novo.");
    }
}

class Projects {
    public void exibir() {
        System.out.println("Meus Projetos");
        System.out.println(" - EasyClean: https://github.com/ggmsbsb/EasyClean");
        System.out.println(" - ColorLens: https://github.com/ggmsbsb/ColorLens");
    }
}

class Skills {
    public void exibir() {
        System.out.println("Habilidades");
        System.out.println(" - Linguagens: Python, Java (17, 21), R");
        System.out.println(" - Análise & Dados: Pandas, NumPy, SciPy, Matplotlib, Seaborn, Plotly, OpenCV, OpenCL");
        System.out.println(" - Machine Learning & Deep Learning: TensorFlow, Keras, Scikit-learn, PCA, K-Means Clustering, Random Forest, PyTorch");
        System.out.println(" - Bancos de Dados: MySQL, PostgreSQL, SQL Server, Firebase");
        System.out.println(" - Desenvolvimento: Spring Framework, Hibernate, Maven, APIs RESTful");
        System.out.println(" - Ferramentas & Outros: Git, Selenium, Beautiful Soup, Power BI");
    }
}

class LinkedIn {
    public void exibir() {
        System.out.println("Conecte-se Comigo");
        System.out.println("Você pode me encontrar no LinkedIn: https://www.linkedin.com/in/guibesb");
    }
}

```

<div align="center">
  <a href="https://www.linkedin.com/in/guibesb">
    <img src="lkd_blink.gif" alt="linkedin" width="150" />
  </a>
</div>
