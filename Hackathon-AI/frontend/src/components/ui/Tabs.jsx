import React from 'react';
export const Tabs = ({ children, value, onValueChange }) => (
    <div>
        <div className="flex border-b border-slate-700">{React.Children.map(children, child => child.type.name === 'TabsList' && React.cloneElement(child, { value, onValueChange }))}</div>
        {React.Children.map(children, child => child.type.name === 'TabsContent' && child.props.value === value ? child : null)}
    </div>
);
export const TabsList = ({ children, value, onValueChange }) => <div className="flex items-center -mb-px">{React.Children.map(children, child => child.type.name === 'TabsTrigger' && React.cloneElement(child, { isActive: child.props.value === value, onClick: () => onValueChange(child.props.value) }))}</div>;
export const TabsTrigger = ({ children, isActive, onClick }) => <button onClick={onClick} className={`px-4 py-3 font-semibold border-b-2 transition-all duration-300 ${isActive ? 'text-blue-400 border-blue-400' : 'text-slate-400 border-transparent hover:text-white'}`}>{children}</button>;
export const TabsContent = ({ children }) => <div className="py-6">{children}</div>;

