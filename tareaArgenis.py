class WorkforcePlanner:
    def __init__(self, demands, hire_fixed_cost=400, hire_var_cost=200, excess_cost=300):
        """
        Inicializa el planificador de fuerza de trabajo.
        
        :param demands: Lista de demandas de trabajadores por semana
        :param hire_fixed_cost: Costo fijo por contratación
        :param hire_var_cost: Costo variable por trabajador contratado
        :param excess_cost: Costo por mantener trabajador excedente por semana
        """
        self.demands = demands
        self.hire_fixed = hire_fixed_cost
        self.hire_var = hire_var_cost
        self.excess_cost = excess_cost
        self.num_weeks = len(demands)
        self.max_demand = max(demands)
        self.cost_table = [[float('inf')] * (self.max_demand + 1) for _ in range(self.num_weeks)]
        self.decision_table = [[0] * (self.max_demand + 1) for _ in range(self.num_weeks)]
        
    def calculate_hiring_cost(self, workers_needed, prev_workers):
        """
        Calcula el costo de contratar trabajadores.
        
        :param workers_needed: Número de trabajadores necesarios
        :param prev_workers: Número de trabajadores en la semana anterior
        """
        if workers_needed <= prev_workers:
            return 0
        return self.hire_fixed + self.hire_var * (workers_needed - prev_workers)
    
    def calculate_excess_cost(self, workers, week):
        """
        Calcula el costo de mantener trabajadores excedentes.
        
        :param workers: Número de trabajadores actuales
        :param week: Semana actual (índice)
        """
        demand = self.demands[week]
        if workers >= demand:
            return self.excess_cost * (workers - demand)
        return float('inf')  # No se permite tener menos trabajadores que la demanda
    
    def find_min_cost_plan(self):
        """
        Encuentra el plan de costo mínimo usando programación dinámica.
        """
        # Inicializar la primera semana
        for workers in range(self.demands[0], self.max_demand + 1):
            hire_cost = self.calculate_hiring_cost(workers, 0)
            excess_cost = self.calculate_excess_cost(workers, 0)
            self.cost_table[0][workers] = hire_cost + excess_cost
            self.decision_table[0][workers] = workers
        
        # Llenar la tabla para las semanas restantes
        for week in range(1, self.num_weeks):
            for current_workers in range(self.demands[week], self.max_demand + 1):
                min_cost = float('inf')
                best_prev_workers = 0
                
                for prev_workers in range(self.demands[week-1], self.max_demand + 1):
                    # Costo de transición de prev_workers a current_workers
                    hire_cost = self.calculate_hiring_cost(current_workers, prev_workers)
                    excess_cost = self.calculate_excess_cost(current_workers, week)
                    total_cost = self.cost_table[week-1][prev_workers] + hire_cost + excess_cost
                    
                    if total_cost < min_cost:
                        min_cost = total_cost
                        best_prev_workers = prev_workers
                
                self.cost_table[week][current_workers] = min_cost
                self.decision_table[week][current_workers] = best_prev_workers
        
        # Encontrar la solución óptima
        final_week = self.num_weeks - 1
        min_final_cost = min(self.cost_table[final_week][self.demands[final_week]:])
        optimal_workers = self.cost_table[final_week].index(min_final_cost)
        
        # Reconstruir el plan óptimo
        plan = []
        current_workers = optimal_workers
        for week in range(self.num_weeks - 1, -1, -1):
            plan.append((week + 1, self.demands[week], current_workers))
            current_workers = self.decision_table[week][current_workers]
        plan.reverse()
        
        return min_final_cost, plan
    
    def print_solution(self):
        """Imprime la solución paso a paso."""
        min_cost, optimal_plan = self.find_min_cost_plan()
        
        print("Solución óptima encontrada:")
        print(f"Costo total mínimo: ${min_cost}")
        print("\nDetalle semana por semana:")
        print("Semana | Demanda | Trabajadores | Costo Contratación | Costo Excedente | Costo Acumulado")
        print("-------|---------|--------------|--------------------|-----------------|----------------")
        
        for i, (week, demand, workers) in enumerate(optimal_plan):
            # Calcular costos para esta semana
            if i == 0:
                hire_cost = self.calculate_hiring_cost(workers, 0)
                prev_workers = 0
            else:
                prev_workers = optimal_plan[i-1][2]
                hire_cost = self.calculate_hiring_cost(workers, prev_workers)
            
            excess_cost = self.calculate_excess_cost(workers, i)
            week_cost = hire_cost + excess_cost
            accum_cost = self.cost_table[i][workers]
            
            print(f"{week:6d} | {demand:7d} | {workers:12d} | ${hire_cost:17d} | ${excess_cost:15d} | ${accum_cost:14d}")


# Datos del problema
demands = [5, 7, 8, 4, 6]  # Demandas semanales

# Crear y ejecutar el planificador
planner = WorkforcePlanner(demands)
planner.print_solution()