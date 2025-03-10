<div align="center">
  <img src="logo_blink.gif" alt="alt text" width="100"/>
</div>

<br/>

```java
public class Portfolio {

    public static void main(String[] args) {
        Portfolio portfolio = new Portfolio();
        portfolio.exibirAboutMe();
        portfolio.exibirProjects();
        portfolio.exibirSkills();
        portfolio.exibirLinkedIn();
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
        System.out.println("A combinação de desenvolvimento, estatística e aprendizado de máquina me empolgou, e desde então, tenho me dedicado a essa área.");
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
        System.out.println("Habilidades e Tecnologias");
        System.out.println(" - Linguagens de Programação: Java, Python, JavaScript");
        System.out.println(" - Frameworks: Spring, TensorFlow, Keras, Flask");
        System.out.println(" - Ferramentas de Análise de Dados: Pandas, NumPy, Matplotlib");
        System.out.println(" - Banco de Dados: MySQL, PostgreSQL, MongoDB");
        System.out.println(" - Outros: Git, Docker");
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