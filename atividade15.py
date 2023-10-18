class CursoTI:
    def __init__(self, nome, vagas):
        self.nome = nome
        self.vagas = vagas
        self.alunos_matriculados = []
        self.professores = []  
        self.horas_semanais = 0
        self.iniciado = False

    def abrir_curso(self):
        if len(self.alunos_matriculados) >= 10:
            self.iniciado = True
            return True
        else:
            print("A turma não pode ser iniciada.\nCurso {} não possui alunos suficientes.".format(self.nome))
            return False

    def matricular_aluno(self, aluno):
        if not self.iniciado and len(self.alunos_matriculados) < self.vagas:
            if aluno not in self.alunos_matriculados and len(aluno.cursos_matriculados) < 2:
                self.alunos_matriculados.append(aluno)
                aluno.cursos_matriculados.append(self)
                return True
        return False

#matricular professor
    def matricular_professor(self, professor):
        if not self.iniciado and professor not in self.professores and professor not in self.professores_dando_aula():
            self.professores.append(professor)
            return True
        return False

    def definir_professor(self, professor):
        if self.iniciado and professor in self.professores:
            if professor.horas_semanais_trabalhadas + self.horas_semanais <= 40:
                self.professores.append(professor)
                professor.horas_semanais_trabalhadas += self.horas_semanais
                return True
        return False

    def professores_dando_aula(self):
        return [p for p in self.professores if self in p.cursos_lecionados]

class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.cursos_matriculados = []

class Professor:
    def __init__(self, nome):
        self.nome = nome
        self.horas_semanais_trabalhadas = 0
        self.cursos_lecionados = [] 

curso_python = CursoTI("Python Avançado", 20)
curso_java = CursoTI("Java Fundamentals", 15)

aluno1 = Aluno("Aline")
aluno2 = Aluno("Bruno")
aluno3 = Aluno("Carla")
aluno4 = Aluno("Daniel")
aluno5 = Aluno("Fabiana")
aluno6 = Aluno("Gabriel")
aluno7 = Aluno("Marcos")
aluno8 = Aluno("Paula")
aluno9 = Aluno("Oliveira")
aluno10 = Aluno("Ricardo")

professor1 = Professor("Berg")


curso_python.horas_semanais = 10

curso_python.matricular_aluno(aluno1)
curso_python.matricular_aluno(aluno2)
curso_python.matricular_aluno(aluno3)
curso_python.matricular_aluno(aluno4)
curso_python.matricular_aluno(aluno5)
curso_python.matricular_aluno(aluno6)
curso_python.matricular_aluno(aluno7)
curso_python.matricular_aluno(aluno8)
curso_python.matricular_aluno(aluno9)
curso_python.matricular_aluno(aluno10)

#matricular professor
curso_python.matricular_professor(professor1)

if curso_python.abrir_curso():
    print(f"Curso {curso_python.nome} aberto!")

if curso_python.definir_professor(professor1):
    print(f"Quantidade de alunos alcançada. O Professor {professor1.nome} foi definido para o curso {curso_python.nome}")
else:
    print(f"Professor {professor1.nome} não pode assumir o curso {curso_python.nome} devido à quantidade de matrículas não alcançada.")


#curso_java.matricular_professor(professor1)
