"""
Professional CRM System with Sidebar Navigation
Customer Relationship Management Portal
"""
from datetime import datetime, date
import yoguido as yog

# ==================== PHOSPHOR ICONS SETUP ====================

# Icon mapping for Phosphor icons - proper icon names for yog.icon()
ICONS = {
    # Navigation
    'dashboard': 'house',
    'contacts': 'users',  
    'leads': 'target',
    'deals': 'handshake',
    'companies': 'buildings',
    'analytics': 'chart-bar',
    'pipeline': 'trend-up',
    'reports': 'file-text',
    'calendar': 'calendar',
    'email': 'envelope',
    'notifications': 'bell',
    'settings': 'gear',
    
    # Actions
    'search': 'magnifying-glass',
    'add': 'plus',
    'edit': 'pencil',
    'delete': 'trash',
    'save': 'floppy-disk',
    'export': 'export',
    'import': 'download',
    'filter': 'funnel',
    
    # Status & Metrics
    'money': 'currency-dollar',
    'trend_up': 'trend-up',
    'trend_down': 'trend-down',
    'check': 'check',
    'clock': 'clock',
    'star': 'star',
    
    # Activity Types
    'phone': 'phone',
    'meeting': 'video-camera',
    'note': 'note',
    'tag': 'tag',
    
    # Profile & User
    'user': 'user',
    'profile': 'user-circle',
    'team': 'users',
    
    # Misc
    'home': 'house',
    'chevron_right': 'caret-right',
    'menu': 'list',
    'close': 'x',
}

# ==================== SAMPLE CRM DATA ====================

contacts_data = [
    {"id": 1, "name": "John Smith", "email": "john.smith@techcorp.com", "phone": "+1-555-0123", "company": "TechCorp Inc", "status": "Active", "last_contact": "2024-01-15", "value": 15000},
    {"id": 2, "name": "Sarah Johnson", "email": "sarah@innovate.co", "phone": "+1-555-0124", "company": "Innovate Solutions", "status": "Prospect", "last_contact": "2024-01-14", "value": 25000},
    {"id": 3, "name": "Mike Chen", "email": "mike.chen@globaltech.com", "phone": "+1-555-0125", "company": "GlobalTech", "status": "Active", "last_contact": "2024-01-13", "value": 45000},
    {"id": 4, "name": "Lisa Rodriguez", "email": "lisa@startupx.io", "phone": "+1-555-0126", "company": "StartupX", "status": "Lead", "last_contact": "2024-01-12", "value": 8000},
    {"id": 5, "name": "David Wilson", "email": "dwilson@enterprise.com", "phone": "+1-555-0127", "company": "Enterprise Corp", "status": "Customer", "last_contact": "2024-01-11", "value": 75000},
]

leads_data = [
    {"id": 1, "name": "Emma Thompson", "email": "emma@bigcorp.com", "source": "Website", "status": "New", "score": 85, "created": "2024-01-15", "value": 12000},
    {"id": 2, "name": "Robert Taylor", "email": "rtaylor@mediumco.com", "source": "Referral", "status": "Qualified", "score": 92, "created": "2024-01-14", "value": 18000},
    {"id": 3, "name": "Alice Brown", "email": "alice@smallbiz.com", "source": "Social Media", "status": "Contacted", "score": 67, "created": "2024-01-13", "value": 5500},
    {"id": 4, "name": "James Wilson", "email": "jwilson@finance.com", "source": "Trade Show", "status": "Proposal", "score": 78, "created": "2024-01-12", "value": 22000},
    {"id": 5, "name": "Maria Garcia", "email": "maria@healthcare.org", "source": "Cold Email", "status": "Negotiation", "score": 89, "created": "2024-01-11", "value": 35000},
]

deals_data = [
    {"id": 1, "title": "Enterprise Software License", "contact": "John Smith", "value": 75000, "stage": "Proposal", "probability": 75, "close_date": "2024-02-15", "created": "2024-01-10"},
    {"id": 2, "title": "Cloud Migration Project", "contact": "Sarah Johnson", "value": 45000, "stage": "Negotiation", "probability": 85, "close_date": "2024-02-20", "created": "2024-01-08"},
    {"id": 3, "title": "Marketing Automation Setup", "contact": "Mike Chen", "value": 25000, "stage": "Discovery", "probability": 45, "close_date": "2024-03-01", "created": "2024-01-05"},
    {"id": 4, "title": "CRM Implementation", "contact": "Lisa Rodriguez", "value": 38000, "stage": "Proposal", "probability": 65, "close_date": "2024-02-28", "created": "2024-01-12"},
    {"id": 5, "title": "Security Audit Service", "contact": "David Wilson", "value": 55000, "stage": "Closed Won", "probability": 100, "close_date": "2024-01-30", "created": "2024-01-01"},
]

companies_data = [
    {"id": 1, "name": "TechCorp Inc", "industry": "Technology", "size": "500-1000", "revenue": "$50M-100M", "contacts": 3, "deals": 2, "status": "Active"},
    {"id": 2, "name": "Innovate Solutions", "industry": "Consulting", "size": "100-500", "revenue": "$10M-50M", "contacts": 2, "deals": 1, "status": "Prospect"},
    {"id": 3, "name": "GlobalTech", "industry": "Software", "size": "1000+", "revenue": "$100M+", "contacts": 4, "deals": 3, "status": "Customer"},
    {"id": 4, "name": "StartupX", "industry": "Fintech", "size": "10-50", "revenue": "$1M-10M", "contacts": 1, "deals": 1, "status": "Lead"},
    {"id": 5, "name": "Enterprise Corp", "industry": "Manufacturing", "size": "1000+", "revenue": "$500M+", "contacts": 5, "deals": 4, "status": "Customer"},
]

crm_stats = {
    'total_contacts': len(contacts_data),
    'active_leads': len([l for l in leads_data if l["status"] in ["New", "Qualified", "Contacted"]]),
    'open_deals': len([d for d in deals_data if d["stage"] != "Closed Won"]),
    'total_pipeline': sum(d["value"] for d in deals_data if d["stage"] != "Closed Won"),
    'monthly_revenue': sum(d["value"] for d in deals_data if d["stage"] == "Closed Won"),
    'conversion_rate': 23.4,
}

recent_activities = [
    {"action": "Call scheduled", "description": "Follow-up call with John Smith", "time": "5m", "type": "phone"},
    {"action": "Deal updated", "description": "Enterprise Software License moved to Proposal", "time": "12m", "type": "deals"},
    {"action": "New lead", "description": "Emma Thompson from BigCorp submitted form", "time": "25m", "type": "leads"},
    {"action": "Email sent", "description": "Proposal sent to Sarah Johnson", "time": "1h", "type": "email"},
    {"action": "Meeting completed", "description": "Discovery call with Mike Chen", "time": "2h", "type": "meeting"},
]

# ==================== CRM SIDEBAR LAYOUT SYSTEM ====================

@yog.layout("crm_sidebar")
def crm_sidebar_layout(page_component):
    """Main CRM layout with sidebar navigation"""
    
    with yog.container(class_name="min-h-screen bg-gray-50 flex"):
        # Sidebar
        render_crm_sidebar()
        
        # Main content area
        with yog.container(class_name="flex-1 flex flex-col"):
            # Top navigation
            render_crm_top_nav()
            
            # Breadcrumb
            render_crm_breadcrumb()
            
            # Page content
            with yog.container(class_name="flex-1 p-6"):
                page_component()

def render_crm_sidebar():
    """Render the CRM sidebar navigation"""
    with yog.container(class_name="w-64 bg-white shadow-lg flex flex-col border-r border-gray-200"):
        # CRM Logo/Header
        with yog.container(class_name="p-6 border-b border-gray-200"):
            yog.title("CRM Pro", level=2, class_name="text-xl font-bold text-purple-600 m-0")
            yog.text("Customer Management", class_name="text-sm text-gray-500 mt-1")
        
        # Navigation menu
        with yog.container(class_name="flex-1 py-6"):
            with yog.container(class_name="px-3 space-y-1"):
                # Main navigation
                sidebar_nav_item("dashboard", "Dashboard", "/crm")
                sidebar_nav_item("contacts", "Contacts", "/crm/contacts")
                sidebar_nav_item("leads", "Leads", "/crm/leads")
                sidebar_nav_item("deals", "Deals", "/crm/deals")
                sidebar_nav_item("companies", "Companies", "/crm/companies")
                
                # Divider
                with yog.container(class_name="my-4"):
                    with yog.container(class_name="border-t border-gray-200"):
                        pass
                
                # Secondary navigation
                yog.text("Analytics & Reports", class_name="px-3 py-2 text-xs font-semibold text-gray-400 uppercase tracking-wider")
                sidebar_nav_item("analytics", "Analytics", "/crm/analytics")
                sidebar_nav_item("pipeline", "Sales Pipeline", "/crm/pipeline")
                sidebar_nav_item("reports", "Reports", "/crm/reports")
                
                # Divider
                with yog.container(class_name="my-4"):
                    with yog.container(class_name="border-t border-gray-200"):
                        pass
                
                # Tools & Settings
                yog.text("Tools & Settings", class_name="px-3 py-2 text-xs font-semibold text-gray-400 uppercase tracking-wider")
                sidebar_nav_item("calendar", "Calendar", "/crm/calendar")
                sidebar_nav_item("email", "Email Center", "/crm/email")
                sidebar_nav_item("notifications", "Notifications", "/crm/notifications")
                sidebar_nav_item("settings", "Settings", "/crm/settings")
        
        # User profile section
        with yog.container(class_name="p-4 border-t border-gray-200 bg-gray-50"):
            with yog.container(class_name="flex items-center space-x-3"):
                with yog.container(class_name="w-8 h-8 bg-purple-600 rounded-full flex items-center justify-center"):
                    yog.icon(ICONS['profile'], weight="regular", size="14px", class_name="text-white")
                
                with yog.container(class_name="flex-1 min-w-0"):
                    yog.text("Sales Manager", class_name="text-sm font-medium text-gray-900 truncate")
                    yog.text("Online", class_name="text-xs text-green-600")

def sidebar_nav_item(icon_key: str, label: str, path: str):
    """Individual sidebar navigation item"""
    is_active = yog.is_current_page(path)
    
    def navigate():
        yog.navigate_to(path)
        print(f"✅ CRM Navigation: {label}")
        yog.alert(f"Navigating to {label}", type="info")
    
    # Style based on active state
    if is_active:
        item_class = "flex items-center space-x-3 px-3 py-2 text-sm font-medium text-purple-600 bg-purple-50 border-r-2 border-purple-600 rounded-l-md w-full text-left"
    else:
        item_class = "flex items-center space-x-3 px-3 py-2 text-sm font-medium text-gray-600 hover:text-gray-900 hover:bg-gray-50 rounded-md transition-colors w-full text-left"
    
    # Create button with icon and text
    with yog.container(class_name="w-full"):
        with yog.container(class_name=item_class):
            yog.icon(ICONS[icon_key], weight="regular", size="16px", class_name="text-current")
            clicked = yog.button(label, on_click=navigate, class_name="text-current bg-transparent border-0 p-0 font-medium text-sm cursor-pointer")
            if clicked:
                return True
    return False

def render_crm_top_nav():
    """Render the CRM top navigation bar"""
    with yog.container(class_name="bg-white shadow-sm border-b border-gray-200 px-6 py-4"):
        with yog.container(class_name="flex items-center justify-between"):
            # Search bar
            with yog.container(class_name="flex items-center space-x-4"):
                yog.input_text(placeholder="Search contacts, deals, companies...", 
                             class_name="w-96 px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500")
                
                def quick_search():
                    yog.alert("Quick search activated", type="info")
                    return True

                # Search button - using crm_button helper
                crm_button("", on_click=quick_search, variant="primary", icon_key="search", size="sm")
            
            # Quick actions
            with yog.container(class_name="flex items-center space-x-3"):
                def add_contact():
                    yog.alert("Add contact modal", type="success")
                    return True
                
                def add_deal():
                    yog.alert("Add deal modal", type="success")
                    return True
                
                def profile_menu():
                    yog.alert("Profile menu opened", type="info")
                    return True
                
                # Add Contact button
                crm_button("Contact", on_click=add_contact, variant="success", icon_key="add", size="sm")
                
                # Add Deal button
                crm_button("Deal", on_click=add_deal, variant="info", icon_key="add", size="sm")
                
                # Profile menu
                crm_button("", on_click=profile_menu, variant="ghost", icon_key="profile", size="sm")

def render_crm_breadcrumb():
    """Render CRM breadcrumb navigation"""
    current_path = yog.get_current_path()
    
    breadcrumb_data = {
        "/crm": [{"label": "Dashboard"}],
        "/crm/contacts": [{"label": "Dashboard", "url": "/crm"}, {"label": "Contacts"}],
        "/crm/leads": [{"label": "Dashboard", "url": "/crm"}, {"label": "Leads"}],
        "/crm/deals": [{"label": "Dashboard", "url": "/crm"}, {"label": "Deals"}],
        "/crm/companies": [{"label": "Dashboard", "url": "/crm"}, {"label": "Companies"}],
        "/crm/analytics": [{"label": "Dashboard", "url": "/crm"}, {"label": "Analytics"}],
        "/crm/pipeline": [{"label": "Dashboard", "url": "/crm"}, {"label": "Sales Pipeline"}],
        "/crm/reports": [{"label": "Dashboard", "url": "/crm"}, {"label": "Reports"}],
        "/crm/calendar": [{"label": "Dashboard", "url": "/crm"}, {"label": "Calendar"}],
        "/crm/email": [{"label": "Dashboard", "url": "/crm"}, {"label": "Email Center"}],
        "/crm/notifications": [{"label": "Dashboard", "url": "/crm"}, {"label": "Notifications"}],
        "/crm/settings": [{"label": "Dashboard", "url": "/crm"}, {"label": "Settings"}]
    }
    
    items = breadcrumb_data.get(current_path, [{"label": "Dashboard"}])
    with yog.container(class_name="bg-white rounded-lg border border-gray-200 px-4 py-3"):
        with yog.container(class_name="flex items-center space-x-2 text-sm"):
            # Home icon
            yog.icon(ICONS['home'], weight="regular", size="16px", class_name="text-gray-400")
            
            for i, item in enumerate(items):
                if i > 0:
                    yog.icon(ICONS['chevron_right'], weight="regular", size="12px", class_name="text-gray-300")
                
                if "url" in item:
                    def navigate_breadcrumb(url=item["url"]):
                        yog.navigate_to(url)
                    
                    clicked = yog.button(item["label"], on_click=navigate_breadcrumb, 
                                    class_name="text-purple-600 hover:text-purple-800 font-medium")
                    if clicked:
                        yog.alert(f"Navigating to {item['label']}", type="info")
                else:
                    yog.text(item["label"], class_name="text-gray-700 font-medium")

# ==================== CRM COMPONENTS ====================

def crm_stats_card(title: str, value: str, change: str = None, trend: str = "neutral", icon_key: str = "analytics", subtitle: str = ""):
    """CRM statistics card"""
    
    trend_colors = {
        "up": "bg-green-50 border-green-200",
        "down": "bg-red-50 border-red-200", 
        "neutral": "bg-blue-50 border-blue-200"
    }
    
    card_class = f"bg-white rounded-lg border-2 {trend_colors.get(trend, 'border-gray-200')} p-6 hover:shadow-md transition-shadow"
    
    with yog.container(class_name=card_class):
        with yog.container(class_name="flex items-center justify-between"):
            with yog.container():
                yog.text(title, class_name="text-sm font-medium text-gray-600")
                yog.text(value, class_name="text-2xl font-bold text-gray-900 mt-1")
                if subtitle:
                    yog.text(subtitle, class_name="text-xs text-gray-500 mt-1")
                if change:
                    change_color = "text-green-600" if trend == "up" else "text-red-600" if trend == "down" else "text-gray-600"
                    yog.text(change, class_name=f"text-sm {change_color} mt-2")
            
            yog.icon(ICONS[icon_key], weight="regular", size="32px", class_name="text-purple-600")

def crm_button(label: str, on_click=None, variant: str = "primary", icon_key: str = "", size: str = "md"):
    """CRM styled button component"""
    
    base_classes = "inline-flex items-center justify-center font-medium rounded-lg transition-colors focus:outline-none focus:ring-2 focus:ring-offset-2"
    
    variant_classes = {
        "primary": "bg-purple-600 text-white hover:bg-purple-700 focus:ring-purple-500",
        "secondary": "bg-gray-200 text-gray-900 hover:bg-gray-300 focus:ring-gray-500",
        "success": "bg-green-600 text-white hover:bg-green-700 focus:ring-green-500",
        "danger": "bg-red-600 text-white hover:bg-red-700 focus:ring-red-500",
        "warning": "bg-yellow-600 text-white hover:bg-yellow-700 focus:ring-yellow-500",
        "info": "bg-blue-600 text-white hover:bg-blue-700 focus:ring-blue-500",
        "ghost": "bg-transparent text-gray-400 hover:text-gray-500 hover:bg-gray-100 focus:ring-gray-500"
    }
    
    size_classes = {
        "sm": "px-3 py-2 text-sm",
        "md": "px-4 py-2 text-sm", 
        "lg": "px-6 py-3 text-base"
    }
    
    button_class = f"{base_classes} {variant_classes.get(variant, variant_classes['primary'])} {size_classes.get(size, size_classes['md'])}"
    
    # Determine button text
    button_text = label if label else "Action"
    if icon_key and not label:
        # Icon-only buttons get descriptive text
        icon_labels = {
            "search": "Search",
            "add": "Add", 
            "profile": "Profile",
            "user": "Contact",
            "deals": "Deal"
        }
        button_text = icon_labels.get(icon_key, "Action")
    
    # Create the button with text as first positional parameter
    clicked = yog.button(button_text, on_click=on_click, class_name=button_class)
    return clicked

def crm_data_table(data, columns, title="Data Table", actions=None):
    """CRM data table component"""
    with yog.container(class_name="bg-white rounded-lg border border-gray-200 overflow-hidden"):
        # Table header
        with yog.container(class_name="px-6 py-4 border-b border-gray-200 bg-gray-50"):
            yog.title(title, level=3, class_name="text-lg font-semibold text-gray-900 m-0")
        
        # Table content
        with yog.container(class_name="overflow-x-auto"):
            yog.table(data, columns=columns, actions=actions, 
                    class_name="w-full divide-y divide-gray-200")

def activity_timeline_item(action: str, description: str, time: str, activity_type: str = "default"):
    """Activity timeline item component"""
    
    type_icons = {
        "phone": "phone",
        "email": "email", 
        "meeting": "meeting",
        "deals": "deals",
        "leads": "leads",
        "default": "note"
    }
    
    type_colors = {
        "phone": "bg-blue-500",
        "email": "bg-green-500",
        "meeting": "bg-purple-500", 
        "deals": "bg-orange-500",
        "leads": "bg-yellow-500",
        "default": "bg-gray-500"
    }
    
    with yog.container(class_name="flex items-start space-x-3 py-4 border-b border-gray-100 last:border-b-0"):
        # Activity indicator
        with yog.container(class_name="flex-shrink-0 mt-1.5"):
            icon_color = type_colors.get(activity_type, "bg-gray-500")
            with yog.container(class_name=f"w-8 h-8 {icon_color} rounded-full flex items-center justify-center"):
                icon_key = type_icons.get(activity_type, "note")
                yog.icon(ICONS[icon_key], weight="regular", size="14px", class_name="text-white")
        
        # Activity content
        with yog.container(class_name="flex-1 min-w-0"):
            yog.text(action, class_name="text-sm font-medium text-gray-900")
            yog.text(description, class_name="text-sm text-gray-500 mt-1")
        
        # Timestamp
        yog.text(time, class_name="flex-shrink-0 text-xs text-gray-400 mt-1.5")

def pipeline_stage_card(stage: str, deals_count: int, total_value: int, color: str = "purple"):
    """Pipeline stage card component"""
    
    color_classes = {
        "purple": "bg-purple-50 border-purple-200 text-purple-800",
        "blue": "bg-blue-50 border-blue-200 text-blue-800",
        "green": "bg-green-50 border-green-200 text-green-800",
        "orange": "bg-orange-50 border-orange-200 text-orange-800",
        "red": "bg-red-50 border-red-200 text-red-800"
    }
    
    card_class = f"rounded-lg border-2 p-4 {color_classes.get(color, color_classes['purple'])}"
    
    with yog.container(class_name=card_class):
        yog.text(stage, class_name="font-semibold text-lg mb-2")
        yog.text(f"{deals_count} deals", class_name="text-sm opacity-75")
        yog.text(f"${total_value:,}", class_name="text-xl font-bold mt-1")

# ==================== CRM PAGES ====================

@yog.page("/crm", title="CRM Dashboard", layout="crm_sidebar")
def crm_dashboard():
    """CRM Dashboard with sidebar layout"""
    
    # Page header
    with yog.container(class_name="mb-8"):
        yog.title("CRM Dashboard", level=1, class_name="text-3xl font-bold text-gray-900")
        yog.text("Track your sales performance and customer relationships", 
                class_name="text-lg text-gray-600 mt-2")
    
    # Key metrics
    with yog.container(class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8"):
        crm_stats_card("Total Contacts", str(crm_stats['total_contacts']), "+12%", "up", "contacts")
        crm_stats_card("Active Leads", str(crm_stats['active_leads']), "+23%", "up", "leads")
        crm_stats_card("Open Deals", str(crm_stats['open_deals']), "+8%", "up", "deals")
        crm_stats_card("Pipeline Value", f"${crm_stats['total_pipeline']:,}", "+15%", "up", "money")
    
    # Main content grid
    with yog.container(class_name="grid grid-cols-1 lg:grid-cols-3 gap-8"):
        
        # Sales pipeline overview (spans 2 columns)
        with yog.container(class_name="lg:col-span-2"):
            with yog.container(class_name="bg-white rounded-lg border border-gray-200"):
                with yog.container(class_name="px-6 py-4 border-b border-gray-200"):
                    yog.title("Sales Pipeline", level=3, class_name="text-lg font-semibold text-gray-900 m-0")
                
                with yog.container(class_name="p-6"):
                    # Pipeline stages
                    with yog.container(class_name="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6"):
                        pipeline_stage_card("Discovery", 3, 83000, "blue")
                        pipeline_stage_card("Proposal", 2, 113000, "orange") 
                        pipeline_stage_card("Negotiation", 1, 45000, "green")
                    
                    # Recent deals
                    yog.text("Recent Deals", class_name="text-sm font-semibold text-gray-700 mb-4")
                    for deal in deals_data[:3]:
                        with yog.container(class_name="flex items-center justify-between py-2 border-b border-gray-100 last:border-b-0"):
                            with yog.container():
                                yog.text(deal["title"], class_name="text-sm font-medium text-gray-900")
                                yog.text(f"{deal['contact']} • {deal['stage']}", class_name="text-xs text-gray-500")
                            yog.text(f"${deal['value']:,}", class_name="text-sm font-semibold text-green-600")
        
        # Recent activity (1 column)
        with yog.container():
            with yog.container(class_name="bg-white rounded-lg border border-gray-200"):
                with yog.container(class_name="px-6 py-4 border-b border-gray-200"):
                    yog.title("Recent Activity", level=3, class_name="text-lg font-semibold text-gray-900 m-0")
                
                with yog.container(class_name="p-6"):
                    for activity in recent_activities:
                        activity_timeline_item(
                            activity["action"], 
                            activity["description"], 
                            activity["time"], 
                            activity["type"]
                        )
    
    # Quick actions section
    with yog.container(class_name="mt-8"):
        with yog.container(class_name="bg-white rounded-lg border border-gray-200"):
            with yog.container(class_name="px-6 py-4 border-b border-gray-200"):
                yog.title("Quick Actions", level=3, class_name="text-lg font-semibold text-gray-900 m-0")
            
            with yog.container(class_name="p-6"):
                with yog.container(class_name="grid grid-cols-1 md:grid-cols-4 gap-4"):
                    def create_contact():
                        yog.alert("Create contact form", type="success")
                        return True
                    
                    def schedule_call():
                        yog.alert("Schedule call", type="info")
                        return True
                    
                    def send_email():
                        yog.alert("Email composer", type="info")
                        return True
                    
                    def create_deal():
                        yog.alert("Create deal form", type="success")
                        return True
                    
                    if crm_button("Add Contact", on_click=create_contact, icon_key="user"):
                        yog.alert("Opening contact form...", type="success")
                    
                    if crm_button("Schedule Call", on_click=schedule_call, icon_key="phone", variant="secondary"):
                        yog.alert("Opening calendar...", type="info")
                    
                    if crm_button("Send Email", on_click=send_email, icon_key="email", variant="secondary"):
                        yog.alert("Opening email composer...", type="info")
                    
                    if crm_button("Create Deal", on_click=create_deal, icon_key="deals", variant="success"):
                        yog.alert("Opening deal form...", type="success")

@yog.page("/crm/contacts", title="Contacts", layout="crm_sidebar")
def crm_contacts():
    """Contact management page"""
    
    # Page header with action
    with yog.container(class_name="mb-8"):
        with yog.container(class_name="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4"):
            with yog.container():
                yog.title("Contact Management", level=1, class_name="text-3xl font-bold text-gray-900")
                yog.text("Manage your customer and prospect relationships", 
                        class_name="text-lg text-gray-600 mt-2")
            
            def add_contact():
                yog.alert("Add contact modal would open", type="info")
                return True
            
            if crm_button("Add Contact", on_click=add_contact, variant="primary", icon_key="user"):
                yog.alert("Opening contact creation form...", type="success")
        
    # Contact statistics
    with yog.container(class_name="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8"):
        crm_stats_card("Total Contacts", str(len(contacts_data)), "+5", "up", "contacts")
        crm_stats_card("Active", str(len([c for c in contacts_data if c["status"] == "Active"])), "+3", "up", "check")
        crm_stats_card("Prospects", str(len([c for c in contacts_data if c["status"] == "Prospect"])), "+2", "up", "leads")
        crm_stats_card("Avg. Value", f"${sum(c['value'] for c in contacts_data)//len(contacts_data):,}", "+8%", "up", "money")
    
    # Search and filters
    with yog.container(class_name="bg-white rounded-lg border border-gray-200 p-4 mb-6"):
        with yog.container(class_name="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4"):
            # Search and filters
            with yog.container(class_name="flex flex-col sm:flex-row gap-4"):
                yog.input_text(placeholder="Search contacts...",
                             class_name="w-full sm:w-80 px-4 py-2 border border-gray-300 rounded-lg")
                yog.select(options=["All Status", "Active", "Prospect", "Lead", "Customer"], 
                         value="All Status",
                         class_name="px-4 py-2 border border-gray-300 rounded-lg")
            
            # Export/Import actions
            with yog.container(class_name="flex gap-3"):
                def export_contacts():
                    yog.alert("Exporting contacts...", type="success")
                    return True
                
                def import_contacts():
                    yog.alert("Import contacts dialog", type="info")
                    return True
                
                if crm_button("Export", on_click=export_contacts, variant="secondary", icon_key="export", size="sm"):
                    yog.alert("Contact data exported!", type="success")
                
                if crm_button("Import", on_click=import_contacts, variant="secondary", icon_key="import", size="sm"):
                    yog.alert("Import dialog opened", type="info")
    
    # Contacts table
    crm_data_table(contacts_data, ["name", "email", "company", "status", "last_contact", "value"], "All Contacts")

@yog.page("/crm/leads", title="Leads", layout="crm_sidebar")
def crm_leads():
    """Lead management page"""
    
    # Page header
    with yog.container(class_name="mb-8"):
        with yog.container(class_name="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4"):
            with yog.container():
                yog.title("Lead Management", level=1, class_name="text-3xl font-bold text-gray-900")
                yog.text("Track and nurture your sales leads", 
                        class_name="text-lg text-gray-600 mt-2")
            
            def add_lead():
                yog.alert("Add lead modal", type="info")
                return True
            
            if crm_button("Add Lead", on_click=add_lead, variant="primary", icon_key="leads"):
                yog.alert("Opening lead creation form...", type="success")
    
    # Lead statistics
    with yog.container(class_name="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8"):
        crm_stats_card("Total Leads", str(len(leads_data)), "+8", "up", "leads")
        crm_stats_card("Qualified", str(len([l for l in leads_data if l["status"] == "Qualified"])), "+2", "up", "check")
        crm_stats_card("In Progress", str(len([l for l in leads_data if l["status"] in ["Contacted", "Proposal"]])), "+3", "up", "pipeline")
        crm_stats_card("Avg. Score", "80", "+5", "up", "star")
    
    # Leads table
    crm_data_table(leads_data, ["name", "email", "source", "status", "score", "value"], "All Leads")

@yog.page("/crm/deals", title="Deals", layout="crm_sidebar")
def crm_deals():
    """Deal management page"""
    
    # Page header
    with yog.container(class_name="mb-8"):
        with yog.container(class_name="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4"):
            with yog.container():
                yog.title("Deal Management", level=1, class_name="text-3xl font-bold text-gray-900")
                yog.text("Track your sales opportunities and pipeline", 
                        class_name="text-lg text-gray-600 mt-2")
            
            def add_deal():
                yog.alert("Add deal modal", type="info")
                return True
            
            if crm_button("Add Deal", on_click=add_deal, variant="primary", icon_key="deals"):
                yog.alert("Opening deal creation form...", type="success")
    
    # Deal statistics
    with yog.container(class_name="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8"):
        crm_stats_card("Total Deals", str(len(deals_data)), "+3", "up", "deals")
        crm_stats_card("Open Deals", str(len([d for d in deals_data if d["stage"] != "Closed Won"])), "+2", "up", "pipeline")
        crm_stats_card("Won Deals", str(len([d for d in deals_data if d["stage"] == "Closed Won"])), "+1", "up", "check")
        crm_stats_card("Win Rate", "65%", "+5%", "up", "star")
    
    # Deals table
    crm_data_table(deals_data, ["title", "contact", "value", "stage", "probability", "close_date"], "All Deals")

@yog.page("/crm/companies", title="Companies", layout="crm_sidebar")
def crm_companies():
    """Company management page"""
    
    # Page header
    with yog.container(class_name="mb-8"):
        with yog.container(class_name="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4"):
            with yog.container():
                yog.title("Company Management", level=1, class_name="text-3xl font-bold text-gray-900")
                yog.text("Manage your business relationships and accounts", 
                        class_name="text-lg text-gray-600 mt-2")
            
            def add_company():
                yog.alert("Add company modal", type="info")
                return True
            
            if crm_button("Add Company", on_click=add_company, variant="primary", icon_key="companies"):
                yog.alert("Opening company creation form...", type="success")
    
    # Company statistics
    with yog.container(class_name="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8"):
        crm_stats_card("Total Companies", str(len(companies_data)), "+2", "up", "companies")
        crm_stats_card("Active Customers", str(len([c for c in companies_data if c["status"] == "Customer"])), "+1", "up", "check")
        crm_stats_card("Prospects", str(len([c for c in companies_data if c["status"] == "Prospect"])), "+1", "up", "leads")
        crm_stats_card("Avg. Contacts", "3.2", "+0.5", "up", "user")
    
    # Industry breakdown
    with yog.container(class_name="bg-white rounded-lg border border-gray-200 mb-6"):
        with yog.container(class_name="px-6 py-4 border-b border-gray-200"):
            yog.title("Industry Breakdown", level=3, class_name="text-lg font-semibold text-gray-900 m-0")
        
        with yog.container(class_name="p-6"):
            # Count companies by industry
            industries = {}
            for company in companies_data:
                industry = company["industry"]
                industries[industry] = industries.get(industry, 0) + 1
            
            with yog.container(class_name="grid grid-cols-1 md:grid-cols-4 gap-4"):
                for industry, count in industries.items():
                    with yog.container(class_name="text-center p-4 bg-gray-50 rounded-lg"):
                        yog.text(str(count), class_name="text-2xl font-bold text-purple-600")
                        yog.text(industry, class_name="text-sm text-gray-600")
    
    # Companies table
    crm_data_table(companies_data, ["name", "industry", "size", "contacts", "deals", "status"], "All Companies")

@yog.page("/crm/analytics", title="Analytics", layout="crm_sidebar")
def crm_analytics():
    """CRM Analytics page"""
    
    # Page header
    with yog.container(class_name="mb-8"):
        yog.title("CRM Analytics", level=1, class_name="text-3xl font-bold text-gray-900")
        yog.text("Analyze your sales performance and customer data", 
                class_name="text-lg text-gray-600 mt-2")
    
    # Key performance metrics
    with yog.container(class_name="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8"):
        crm_stats_card("Total Revenue", f"${crm_stats['monthly_revenue']:,}", "+18.5%", "up", "money")
        crm_stats_card("Pipeline Value", f"${crm_stats['total_pipeline']:,}", "+12.3%", "up", "analytics")
        crm_stats_card("Conversion Rate", f"{crm_stats['conversion_rate']}%", "+2.1%", "up", "pipeline")
        crm_stats_card("Avg. Deal Time", "32 days", "-3 days", "up", "clock")
    
    # Charts section
    with yog.container(class_name="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-8"):
        
        # Revenue trend chart
        with yog.container(class_name="bg-white rounded-lg border border-gray-200"):
            with yog.container(class_name="px-6 py-4 border-b border-gray-200"):
                yog.title("Revenue Trend", level=3, class_name="text-lg font-semibold text-gray-900 m-0")
            
            with yog.container(class_name="p-6"):
                # Sample revenue data
                revenue_data = [
                    {"month": "Jan", "revenue": 45000},
                    {"month": "Feb", "revenue": 52000},
                    {"month": "Mar", "revenue": 48000},
                    {"month": "Apr", "revenue": 58000},
                    {"month": "May", "revenue": 62000},
                ]
                yog.line_chart(data=revenue_data, x_key="month", y_key="revenue", 
                             title="Monthly Revenue")
        
        # Deal conversion funnel
        with yog.container(class_name="bg-white rounded-lg border border-gray-200"):
            with yog.container(class_name="px-6 py-4 border-b border-gray-200"):
                yog.title("Conversion Funnel", level=3, class_name="text-lg font-semibold text-gray-900 m-0")
            
            with yog.container(class_name="p-6"):
                # Sample funnel data
                funnel_data = [
                    {"stage": "Leads", "count": 150},
                    {"stage": "Qualified", "count": 85},
                    {"stage": "Proposal", "count": 45},
                    {"stage": "Negotiation", "count": 28},
                    {"stage": "Closed Won", "count": 18},
                ]
                yog.bar_chart(data=funnel_data, x_key="stage", y_key="count", 
                            title="Sales Funnel")
    
    # Coming soon placeholder
    with yog.container(class_name="bg-white rounded-lg border border-gray-200"):
        with yog.container(class_name="p-12 text-center"):
            yog.icon(ICONS['analytics'], weight="regular", size="64px", class_name="mb-4 text-purple-600")
            yog.title("Advanced Analytics", level=2, class_name="text-2xl font-semibold text-gray-900 mb-2")
            yog.text("Detailed analytics and reporting features coming soon!", 
                    class_name="text-gray-600 mb-6")
            
            def notify_analytics():
                yog.alert("You'll be notified when advanced analytics are ready!", type="success")
                return True
            
            if crm_button("Notify Me", on_click=notify_analytics, variant="secondary", icon_key="notifications"):
                yog.alert("Analytics notification preferences updated!", type="success")

# Additional placeholder pages
@yog.page("/crm/pipeline", title="Sales Pipeline", layout="crm_sidebar")
def crm_pipeline():
    """Sales Pipeline page"""
    with yog.container(class_name="text-center py-16"):
        yog.icon(ICONS['pipeline'], weight="regular", size="64px", class_name="mb-4 text-purple-600")
        yog.title("Sales Pipeline", level=1, class_name="text-3xl font-bold text-gray-900 mb-4")
        yog.text("Advanced pipeline management coming soon!", class_name="text-lg text-gray-600")

@yog.page("/crm/reports", title="Reports", layout="crm_sidebar")
def crm_reports():
    """Reports page"""
    with yog.container(class_name="text-center py-16"):
        yog.icon(ICONS['reports'], weight="regular", size="64px", class_name="mb-4 text-purple-600")
        yog.title("Reports", level=1, class_name="text-3xl font-bold text-gray-900 mb-4")
        yog.text("Custom reporting features coming soon!", class_name="text-lg text-gray-600")

@yog.page("/crm/calendar", title="Calendar", layout="crm_sidebar")
def crm_calendar():
    """Calendar page"""
    with yog.container(class_name="text-center py-16"):
        yog.icon(ICONS['calendar'], weight="regular", size="64px", class_name="mb-4 text-purple-600")
        yog.title("Calendar", level=1, class_name="text-3xl font-bold text-gray-900 mb-4")
        yog.text("Calendar integration coming soon!", class_name="text-lg text-gray-600")

@yog.page("/crm/email", title="Email Center", layout="crm_sidebar")
def crm_email():
    """Email Center page"""
    with yog.container(class_name="text-center py-16"):
        yog.icon(ICONS['email'], weight="regular", size="64px", class_name="mb-4 text-purple-600")
        yog.title("Email Center", level=1, class_name="text-3xl font-bold text-gray-900 mb-4")
        yog.text("Email management coming soon!", class_name="text-lg text-gray-600")

@yog.page("/crm/notifications", title="Notifications", layout="crm_sidebar")
def crm_notifications():
    """Notifications page"""
    with yog.container(class_name="text-center py-16"):
        yog.icon(ICONS['notifications'], weight="regular", size="64px", class_name="mb-4 text-purple-600")
        yog.title("Notifications", level=1, class_name="text-3xl font-bold text-gray-900 mb-4")
        yog.text("Notification center coming soon!", class_name="text-lg text-gray-600")

@yog.page("/crm/settings", title="Settings", layout="crm_sidebar")
def crm_settings():
    """CRM Settings page"""
    
    # Page header
    with yog.container(class_name="mb-8"):
        yog.title("CRM Settings", level=1, class_name="text-3xl font-bold text-gray-900")
        yog.text("Configure your CRM preferences and system settings", 
                class_name="text-lg text-gray-600 mt-2")
    
    # Settings grid
    with yog.container(class_name="grid grid-cols-1 lg:grid-cols-2 gap-8"):
        
        # General CRM settings
        with yog.container(class_name="bg-white rounded-lg border border-gray-200"):
            with yog.container(class_name="px-6 py-4 border-b border-gray-200"):
                yog.title("General Settings", level=3, class_name="text-lg font-semibold text-gray-900 m-0")
            
            with yog.container(class_name="p-6 space-y-6"):
                with yog.container():
                    yog.text("CRM Name", class_name="block text-sm font-medium text-gray-700 mb-2")
                    yog.input_text(value="CRM Pro", 
                                 class_name="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500")
                
                with yog.container():
                    yog.text("Default Currency", class_name="block text-sm font-medium text-gray-700 mb-2")
                    yog.select(options=["USD", "EUR", "GBP", "CAD"], value="USD", 
                             class_name="w-full px-3 py-2 border border-gray-300 rounded-lg")
                
                with yog.container(class_name="space-y-3"):
                    yog.checkbox("Enable lead scoring", checked=True, 
                               class_name="flex items-center space-x-2")
                    yog.checkbox("Auto-assign leads", checked=False,
                               class_name="flex items-center space-x-2")
                
                def save_crm_settings():
                    yog.alert("CRM settings saved!", type="success")
                    return True
                
                if crm_button("Save Settings", on_click=save_crm_settings, variant="primary", icon_key="save"):
                    yog.alert("Saving CRM settings...", type="info")
        
        # Sales settings
        with yog.container(class_name="bg-white rounded-lg border border-gray-200"):
            with yog.container(class_name="px-6 py-4 border-b border-gray-200"):
                yog.title("Sales Settings", level=3, class_name="text-lg font-semibold text-gray-900 m-0")
            
            with yog.container(class_name="p-6 space-y-6"):
                with yog.container():
                    yog.text("Sales Cycle Length", class_name="block text-sm font-medium text-gray-700 mb-2")
                    yog.select(options=["30 days", "60 days", "90 days", "120 days"], 
                             value="60 days", 
                             class_name="w-full px-3 py-2 border border-gray-300 rounded-lg")
                
                with yog.container(class_name="space-y-3"):
                    yog.checkbox("Enable deal probability tracking", checked=True,
                               class_name="flex items-center space-x-2")
                    yog.checkbox("Require approval for large deals", checked=True,
                               class_name="flex items-center space-x-2")
                    yog.checkbox("Send deal notifications", checked=False,
                               class_name="flex items-center space-x-2")
                
                def save_sales_settings():
                    yog.alert("Sales settings updated!", type="success")
                    return True
                
                if crm_button("Update Sales", on_click=save_sales_settings, variant="success", icon_key="deals"):
                    yog.alert("Updating sales settings...", type="info")

# ==================== MAIN CRM APPLICATION ====================
def main():
    """Main CRM application entry point"""
    
    print("🚀 Starting Professional CRM System...")
    print("=" * 70)
    
    # Database configuration (example)
    db_config = {
        'type': 'postgres',  # or 'postgres'
        'host': 'localhost',
        'port': 5432,     # 5432 for Postgres
        'database': 'crm_system',
        'user': 'postgres',
        'password': '3RD&4rd=5rd'
    }
        
    # Create CRM app
    app = yog.YoGuidoApp("Professional CRM System", debug=True)
    app.enable_router()
    
    # Set initial page
    yog.navigate_to("/crm")
    
    # Show debug info
    app.debug_info()
    
    # Compile and run
    print("🔨 Compiling with Tailwind CSS...")
    app.compile(force=True)
    
    print("🌐 Starting CRM server...")
    print("✨ Open: http://127.0.0.1:8000/crm")
    print("🎨 CRM Features:")
    print("   - Contact Management")
    print("   - Lead Tracking & Scoring")
    print("   - Deal Pipeline Management")
    print("   - Company Profiles")
    print("   - Sales Analytics")
    print("   - Activity Timeline")
    print("   - Quick Actions")
    print("   - Responsive Design")
    print("=" * 70)
    
    app.run(host="127.0.0.1", port=8000)

if __name__ == "__main__":
    main()
