"""
Python ChainMap - Comprehensive Examples
========================================

ChainMap groups multiple dictionaries or mappings together to create a single,
updateable view. It searches through the mappings in the order they are
provided and returns the first match found.
"""

from collections import ChainMap
import os

# 1. Basic ChainMap Creation and Operations
print("=== BASIC CHAINMAP OPERATIONS ===")

# Creating ChainMap
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5, 'f': 6}

chain = ChainMap(dict1, dict2, dict3)
print(f"ChainMap: {chain}")
print(f"ChainMap as dict: {dict(chain)}")

# Accessing values
print(f"Value 'a': {chain['a']}")
print(f"Value 'c': {chain['c']}")
print(f"Value 'e': {chain['e']}")

# Key that exists in multiple mappings (returns first match)
dict1['x'] = 100
dict2['x'] = 200
dict3['x'] = 300

chain_with_duplicates = ChainMap(dict1, dict2, dict3)
print(f"Value 'x' (first match): {chain_with_duplicates['x']}")

# 2. ChainMap Methods and Properties
print("\n=== CHAINMAP METHODS AND PROPERTIES ===")

chain = ChainMap({'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6})

# maps property - returns list of mappings
print(f"Mappings: {chain.maps}")

# new_child() - creates new ChainMap with additional mapping at beginning
new_chain = chain.new_child({'g': 7, 'h': 8})
print(f"New chain with child: {dict(new_chain)}")

# parents property - returns ChainMap without first mapping
parent_chain = new_chain.parents
print(f"Parent chain: {dict(parent_chain)}")

# 3. ChainMap for Configuration Management
print("\n=== CHAINMAP FOR CONFIGURATION MANAGEMENT ===")

class ConfigManager:
    def __init__(self):
        # Default configuration
        self.defaults = {
            'debug': False,
            'port': 8080,
            'host': 'localhost',
            'timeout': 30,
            'log_level': 'INFO'
        }
        
        # Environment-specific configuration
        self.environment = {}
        
        # User-specific configuration
        self.user_config = {}
        
        # Runtime configuration (highest priority)
        self.runtime = {}
        
        # Create ChainMap with priority order
        self.config = ChainMap(self.runtime, self.user_config, self.environment, self.defaults)
    
    def set_environment_config(self, config_dict):
        """Set environment-specific configuration."""
        self.environment.update(config_dict)
        print(f"Environment config updated: {config_dict}")
    
    def set_user_config(self, config_dict):
        """Set user-specific configuration."""
        self.user_config.update(config_dict)
        print(f"User config updated: {config_dict}")
    
    def set_runtime_config(self, config_dict):
        """Set runtime configuration."""
        self.runtime.update(config_dict)
        print(f"Runtime config updated: {config_dict}")
    
    def get_config(self):
        """Get current configuration."""
        return dict(self.config)
    
    def get_config_source(self, key):
        """Get which mapping contains the key."""
        for i, mapping in enumerate(self.config.maps):
            if key in mapping:
                sources = ['runtime', 'user', 'environment', 'defaults']
                return sources[i]
        return None

# Test configuration manager
config_manager = ConfigManager()
print(f"Initial config: {config_manager.get_config()}")

config_manager.set_environment_config({'host': 'staging.example.com', 'debug': True})
config_manager.set_user_config({'timeout': 60, 'log_level': 'DEBUG'})
config_manager.set_runtime_config({'port': 3000})

print(f"Final config: {config_manager.get_config()}")
print(f"Host source: {config_manager.get_config_source('host')}")
print(f"Port source: {config_manager.get_config_source('port')}")
print(f"Timeout source: {config_manager.get_config_source('timeout')}")

# 4. ChainMap for Variable Scope Simulation
print("\n=== CHAINMAP FOR VARIABLE SCOPE SIMULATION ===")

class ScopeManager:
    def __init__(self):
        self.global_scope = {}
        self.scope_stack = [self.global_scope]
    
    def push_scope(self):
        """Push new scope onto stack."""
        new_scope = {}
        self.scope_stack.append(new_scope)
        return new_scope
    
    def pop_scope(self):
        """Pop scope from stack."""
        if len(self.scope_stack) > 1:
            return self.scope_stack.pop()
        return None
    
    def get_current_scope(self):
        """Get current scope as ChainMap."""
        return ChainMap(*reversed(self.scope_stack))
    
    def set_variable(self, name, value):
        """Set variable in current scope."""
        self.scope_stack[-1][name] = value
        print(f"Set {name} = {value} in current scope")
    
    def get_variable(self, name):
        """Get variable from current scope chain."""
        current_scope = self.get_current_scope()
        if name in current_scope:
            return current_scope[name]
        return None

# Test scope manager
scope_manager = ScopeManager()

# Global scope
scope_manager.set_variable('x', 10)
scope_manager.set_variable('y', 20)

print(f"Global scope: {dict(scope_manager.get_current_scope())}")

# Function scope
scope_manager.push_scope()
scope_manager.set_variable('x', 100)  # Shadows global x
scope_manager.set_variable('z', 30)

print(f"Function scope: {dict(scope_manager.get_current_scope())}")
print(f"Variable x: {scope_manager.get_variable('x')}")
print(f"Variable y: {scope_manager.get_variable('y')}")
print(f"Variable z: {scope_manager.get_variable('z')}")

# Nested scope
scope_manager.push_scope()
scope_manager.set_variable('x', 1000)  # Shadows function x
scope_manager.set_variable('w', 40)

print(f"Nested scope: {dict(scope_manager.get_current_scope())}")
print(f"Variable x: {scope_manager.get_variable('x')}")

# Pop scopes
scope_manager.pop_scope()
print(f"After pop: {dict(scope_manager.get_current_scope())}")

scope_manager.pop_scope()
print(f"Back to global: {dict(scope_manager.get_current_scope())}")

# 5. ChainMap for Template Inheritance
print("\n=== CHAINMAP FOR TEMPLATE INHERITANCE ===")

class TemplateEngine:
    def __init__(self):
        self.templates = {}
        self.base_template = {
            'title': 'My Website',
            'header': 'Welcome',
            'footer': '© 2024',
            'css': ['base.css'],
            'js': ['common.js']
        }
    
    def register_template(self, name, template_dict):
        """Register a template."""
        self.templates[name] = template_dict
        print(f"Registered template: {name}")
    
    def render_template(self, template_name):
        """Render template with inheritance."""
        if template_name not in self.templates:
            raise ValueError(f"Template {template_name} not found")
        
        # Create inheritance chain
        template = self.templates[template_name]
        inherited = template.get('extends')
        
        if inherited:
            # Recursively build inheritance chain
            chain_maps = [template]
            current = inherited
            while current and current in self.templates:
                chain_maps.append(self.templates[current])
                current = self.templates[current].get('extends')
            
            # Add base template at the end
            chain_maps.append(self.base_template)
            
            # Create ChainMap for inheritance
            final_template = ChainMap(*chain_maps)
        else:
            # No inheritance, just use template and base
            final_template = ChainMap(template, self.base_template)
        
        return dict(final_template)

# Test template engine
engine = TemplateEngine()

# Register templates
engine.register_template('base', {
    'title': 'Base Template',
    'content': 'Base content'
})

engine.register_template('page', {
    'extends': 'base',
    'title': 'Page Template',
    'content': 'Page content',
    'css': ['page.css']
})

engine.register_template('article', {
    'extends': 'page',
    'title': 'Article Template',
    'content': 'Article content',
    'js': ['article.js', 'comments.js']
})

# Render templates
print("Rendered templates:")
for template_name in ['base', 'page', 'article']:
    rendered = engine.render_template(template_name)
    print(f"{template_name}: {rendered}")

# 6. ChainMap for Command Line Argument Processing
print("\n=== CHAINMAP FOR COMMAND LINE ARGUMENT PROCESSING ===")

class ArgumentProcessor:
    def __init__(self):
        # Default arguments
        self.defaults = {
            'verbose': False,
            'output': 'stdout',
            'format': 'json',
            'timeout': 30
        }
        
        # Configuration file arguments
        self.config_file = {}
        
        # Command line arguments (highest priority)
        self.cli_args = {}
        
        # Create ChainMap
        self.args = ChainMap(self.cli_args, self.config_file, self.defaults)
    
    def load_config_file(self, config_dict):
        """Load configuration from file."""
        self.config_file.update(config_dict)
        print(f"Config file loaded: {config_dict}")
    
    def set_cli_args(self, cli_dict):
        """Set command line arguments."""
        self.cli_args.update(cli_dict)
        print(f"CLI args set: {cli_dict}")
    
    def get_argument(self, key, default=None):
        """Get argument value."""
        return self.args.get(key, default)
    
    def get_all_arguments(self):
        """Get all arguments."""
        return dict(self.args)
    
    def get_argument_source(self, key):
        """Get source of argument."""
        if key in self.cli_args:
            return 'cli'
        elif key in self.config_file:
            return 'config_file'
        elif key in self.defaults:
            return 'defaults'
        else:
            return None

# Test argument processor
processor = ArgumentProcessor()

# Load configuration file
processor.load_config_file({
    'output': 'file',
    'format': 'yaml',
    'log_level': 'DEBUG'
})

# Set command line arguments
processor.set_cli_args({
    'verbose': True,
    'timeout': 60,
    'input': 'data.txt'
})

print(f"All arguments: {processor.get_all_arguments()}")
print(f"Output source: {processor.get_argument_source('output')}")
print(f"Verbose source: {processor.get_argument_source('verbose')}")
print(f"Log level source: {processor.get_argument_source('log_level')}")

# 7. ChainMap for Environment Variable Management
print("\n=== CHAINMAP FOR ENVIRONMENT VARIABLE MANAGEMENT ===")

class EnvironmentManager:
    def __init__(self):
        # Application defaults
        self.defaults = {
            'APP_NAME': 'MyApp',
            'APP_VERSION': '1.0.0',
            'DEBUG': False,
            'PORT': 8080,
            'HOST': 'localhost'
        }
        
        # System environment variables
        self.system_env = dict(os.environ)
        
        # Application-specific environment
        self.app_env = {}
        
        # Runtime overrides
        self.runtime_env = {}
        
        # Create ChainMap
        self.env = ChainMap(self.runtime_env, self.app_env, self.system_env, self.defaults)
    
    def set_app_env(self, env_dict):
        """Set application-specific environment variables."""
        self.app_env.update(env_dict)
        print(f"App env updated: {env_dict}")
    
    def set_runtime_env(self, env_dict):
        """Set runtime environment variables."""
        self.runtime_env.update(env_dict)
        print(f"Runtime env updated: {env_dict}")
    
    def get_env_var(self, key, default=None):
        """Get environment variable."""
        return self.env.get(key, default)
    
    def get_all_env(self):
        """Get all environment variables."""
        return dict(self.env)
    
    def get_env_source(self, key):
        """Get source of environment variable."""
        if key in self.runtime_env:
            return 'runtime'
        elif key in self.app_env:
            return 'app'
        elif key in self.system_env:
            return 'system'
        elif key in self.defaults:
            return 'defaults'
        else:
            return None

# Test environment manager
env_manager = EnvironmentManager()

# Set application environment
env_manager.set_app_env({
    'DEBUG': True,
    'DATABASE_URL': 'postgresql://localhost/mydb'
})

# Set runtime environment
env_manager.set_runtime_env({
    'PORT': 3000,
    'LOG_LEVEL': 'DEBUG'
})

print(f"Environment variables: {env_manager.get_all_env()}")
print(f"DEBUG source: {env_manager.get_env_source('DEBUG')}")
print(f"PORT source: {env_manager.get_env_source('PORT')}")
print(f"APP_NAME source: {env_manager.get_env_source('APP_NAME')}")

# 8. ChainMap for Plugin System
print("\n=== CHAINMAP FOR PLUGIN SYSTEM ===")

class PluginManager:
    def __init__(self):
        self.core_functions = {
            'save': lambda data: f"Core save: {data}",
            'load': lambda data: f"Core load: {data}",
            'delete': lambda data: f"Core delete: {data}"
        }
        
        self.plugins = []
        self.plugin_functions = {}
    
    def register_plugin(self, plugin_name, functions):
        """Register a plugin."""
        self.plugins.append(plugin_name)
        self.plugin_functions[plugin_name] = functions
        print(f"Registered plugin: {plugin_name}")
    
    def get_function(self, function_name):
        """Get function from plugin chain."""
        # Create ChainMap with plugins in reverse order (latest first)
        all_functions = [self.plugin_functions[plugin] for plugin in reversed(self.plugins)]
        all_functions.append(self.core_functions)
        
        function_chain = ChainMap(*all_functions)
        return function_chain.get(function_name)
    
    def execute_function(self, function_name, *args, **kwargs):
        """Execute function from plugin chain."""
        func = self.get_function(function_name)
        if func:
            return func(*args, **kwargs)
        else:
            raise ValueError(f"Function {function_name} not found")

# Test plugin manager
plugin_manager = PluginManager()

# Register plugins
plugin_manager.register_plugin('encryption', {
    'save': lambda data: f"Encrypted save: {data}",
    'encrypt': lambda data: f"Encrypted: {data}"
})

plugin_manager.register_plugin('compression', {
    'save': lambda data: f"Compressed save: {data}",
    'compress': lambda data: f"Compressed: {data}"
})

# Execute functions
print("Function execution:")
print(f"Save: {plugin_manager.execute_function('save', 'test data')}")
print(f"Load: {plugin_manager.execute_function('load', 'test data')}")
print(f"Encrypt: {plugin_manager.execute_function('encrypt', 'test data')}")

# 9. ChainMap for Database Connection Management
print("\n=== CHAINMAP FOR DATABASE CONNECTION MANAGEMENT ===")

class DatabaseManager:
    def __init__(self):
        # Default connection settings
        self.defaults = {
            'host': 'localhost',
            'port': 5432,
            'database': 'myapp',
            'username': 'user',
            'password': 'password',
            'timeout': 30,
            'ssl': False
        }
        
        # Environment-specific settings
        self.environment = {}
        
        # Connection pool settings
        self.pool_settings = {}
        
        # Active connection settings
        self.active_connection = {}
        
        # Create ChainMap
        self.settings = ChainMap(self.active_connection, self.pool_settings, self.environment, self.defaults)
    
    def set_environment(self, env_name):
        """Set environment-specific settings."""
        if env_name == 'development':
            self.environment.update({
                'host': 'dev-db.example.com',
                'database': 'myapp_dev',
                'debug': True
            })
        elif env_name == 'production':
            self.environment.update({
                'host': 'prod-db.example.com',
                'database': 'myapp_prod',
                'ssl': True,
                'timeout': 60
            })
        print(f"Environment set to: {env_name}")
    
    def set_pool_settings(self, pool_dict):
        """Set connection pool settings."""
        self.pool_settings.update(pool_dict)
        print(f"Pool settings updated: {pool_dict}")
    
    def get_connection_string(self):
        """Get database connection string."""
        settings = dict(self.settings)
        return f"postgresql://{settings['username']}:{settings['password']}@{settings['host']}:{settings['port']}/{settings['database']}"
    
    def get_settings(self):
        """Get current settings."""
        return dict(self.settings)

# Test database manager
db_manager = DatabaseManager()

# Set environment
db_manager.set_environment('development')

# Set pool settings
db_manager.set_pool_settings({
    'max_connections': 20,
    'min_connections': 5,
    'connection_timeout': 30
})

print(f"Connection string: {db_manager.get_connection_string()}")
print(f"Settings: {db_manager.get_settings()}")

# 10. ChainMap Performance and Best Practices
print("\n=== CHAINMAP PERFORMANCE AND BEST PRACTICES ===")

import time

def benchmark_chainmap_vs_dict():
    """Benchmark ChainMap vs regular dict operations."""
    
    # Create test data
    dict1 = {f'key{i}': i for i in range(1000)}
    dict2 = {f'key{i}': i * 2 for i in range(500, 1500)}
    dict3 = {f'key{i}': i * 3 for i in range(1000, 2000)}
    
    # ChainMap operations
    chain = ChainMap(dict1, dict2, dict3)
    
    start_time = time.time()
    for i in range(10000):
        _ = chain.get(f'key{i % 2000}', 'default')
    chainmap_time = time.time() - start_time
    
    # Regular dict operations (merged)
    merged_dict = {**dict1, **dict2, **dict3}
    
    start_time = time.time()
    for i in range(10000):
        _ = merged_dict.get(f'key{i % 2000}', 'default')
    dict_time = time.time() - start_time
    
    return chainmap_time, dict_time

chainmap_time, dict_time = benchmark_chainmap_vs_dict()
print(f"ChainMap lookup time: {chainmap_time:.6f}s")
print(f"Dict lookup time: {dict_time:.6f}s")
print(f"ChainMap overhead: {(chainmap_time/dict_time - 1) * 100:.1f}%")

# Best practices
print("\nBest practices for ChainMap:")
print("1. Use ChainMap when you need to maintain separate mappings")
print("2. Regular dict is faster for simple lookups")
print("3. ChainMap is useful for configuration hierarchies")
print("4. Be aware of the search order (first mapping has priority)")
print("5. Use new_child() and parents for dynamic scope management")

print("\n" + "="*50)
print("ChainMap examples completed!")
print("="*50)
