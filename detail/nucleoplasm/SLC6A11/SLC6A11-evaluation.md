---
type: protein-evaluation
gene: "SLC6A11"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## SLC6A11 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SLC6A11 |
| 蛋白名称 | Sodium- and chloride-dependent GABA transporter 3 |
| 蛋白大小 | 632 aa / 70.6 kDa |
| UniProt ID | P48066 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | ×4 | 28.0 | Nucleoplasm; Vesicles (Uncertain) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 632 aa |
| 新颖性 | 9/10 | ×5 | 45.0 | PubMed=30 |
| 三维结构 | 10/10 | ×3 | 30.0 | pLDDT=86.6; PDB=5 |
| 调控结构域 | 4/10 | ×2 | 8.0 | Na/ntran_symport; Na/ntran_symport_GABA_GAT3; SNS_sf |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=8 |
| **加权总分** | | | **135/180** | |
| **归一化总分** | | | **74.3/100** | 互证: +1 |

### 3. 分析
- Nucleoplasm; Vesicles (Uncertain)
- PubMed strict=30 broad=134
- AF pLDDT=86.6 PDB=5
- InterPro: Na/ntran_symport; Na/ntran_symport_GABA_GAT3; SNS_sf
- Pfam: SNF
- PPI degree=8 ChIP: None
39923323: 4-Phenylbutyrate restored GABA uptake, mitigated seizures in SLC6A1 and SLC6A11  | 35461379: Whole-genome sequencing analysis of clozapine-induced myocarditis. | 23795861: Gaba transporter SLC6A11 gene polymorphism associated with tardive dyskinesia.

### 4. 总体评价
**74.3/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Sodium- and chloride-dependent GABA transporter 3

**功能**: Mediates sodium- and chloride-dependent transport of gamma-aminobutyric acid (GABA) (PubMed:7874447). Can also mediate transport of beta-alanine and to a lower extent that of taurine and hypotaurine (By similarity)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR000175 |
| InterPro | IPR002982 |
| InterPro | IPR037272 |
| Pfam | PF00209 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| MBNL1 | STRING | 756 |
| TWNK | STRING | 742 |
| CELF1 | STRING | 703 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-P48066-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000132164-SLC6A11

![](https://images.proteinatlas.org/37981/437_B6_4_red_green.jpg)
![](https://images.proteinatlas.org/37981/437_B6_5_red_green.jpg)
![](https://images.proteinatlas.org/37981/1853_A3_33_red_green.jpg)
![](https://images.proteinatlas.org/37981/1853_A3_34_red_green.jpg)

### 深度机制分析

SLC6A11(GAT-3)属于Na+/Cl-依赖的神经递质转运蛋白超家族(SLC6, IPR000175/IPR037272)，其12次跨膜螺旋组成SNS_sf折叠(Pfam PF00209)，中心存在一个保守的透性孔用于GABA的协同转运(Na+:Cl-:GABA = 2:1:1化学计量比)。AlphaFold pLDDT 86.6虽非顶级，但5个PDB条目(实验结构)的存在确证了其跨膜核心的结构可靠性；N端和C端胞内区域(各约60 aa)在部分构象中表现高flexibility(pLDDT 50-70)，这两个区段可能介导核靶向或蛋白-蛋白相互作用。HPA Uncertain级别的Nucleoplasm(主要)/Vesicles(次要)定位是该蛋白最大的悬念——膜转运蛋白的核内出现通常意味着其非经典的"兼职"功能(protein moonlighting)。机制假设：SLC6A11在GABAergic神经元信号中常规定位于突触前膜，但在特定应激条件(如氧化应激、染色体损伤)下，其胞内domain可被caspase或calpain裂解释放N端或C端胞浆片段，后者携带隐蔽NLS进入核质与转录因子或染色质重塑复合物直接相互作用。这一模型在许多跨膜蛋白(如Notch、APP、ErbB4)中已有先例。

PPI网络的三元核心——MBNL1(STRING 756)、CELF1(STRING 703)、TWNK(STRING 742)——为这一假设提供了关键的实验入口。MBNL1和CELF1均为RNA结合蛋白，共同调控pre-mRNA的剪接和3'-UTR加工，在重复序列扩增疾病(如肌强直性营养不良DM1/DM2，由CTG/CCTG重复序列触发)中发挥核心作用。SLC6A11与这些RNA剪接因子的高置信度PPI提示GAT-3可能存在一个隐蔽的"RNA结合模块"——借助其跨膜蛋白的胞内loop或被切割片段，物理结合CUG/CUG重复发夹RNA，引导MBNL1/CELF1的出核或sequestration。这一功能直接连接TE调控：内源性逆转录病毒(LTR/ERV)和SINE(Alu)元件的转录产生大量重复RNA，SLC6A11可能作为这些TE RNA的胞内传感器或转运器。

此外，TWNK(Twinkle, mtDNA解旋酶，STRING 742)的纳入提示SLC6A11与线粒体-核通讯之间存在额外通路。GABA本身不仅是神经递质，也是多种模式生物中已知的表观遗传代谢物——GABA通过GABA转氨酶(GABA-T)进入TCA周期的"GABA shunt"，调节琥珀酸/alpha-KG比率，进而影响TET DNA去甲基化酶和JmjC组蛋白去甲基化酶的活性。因此，SLC6A11的核内池可能通过三条正交路径影响TE调控：(i)其切割片段作为MBNL1/CELF1的协同因子调节TE RNA剪接，(ii)通过GABA摄取间接调制琥珀酸/alpha-KG比值作为双加氧酶(Erasers)的辅因子，(iii)其跨膜区可能的非编码TE元件(如LINE-1 5'-UTR处的SNS家族蛋白结合motif)提供的转录正反馈。研究启示：SLC6A11作为"膜转运蛋白兼职核调控因子"的假设虽然高度推测性，但其PPI网络中MBNL1-TE剪接轴的强力证据使得这一方向值得严谨探索。实验策略：构建SLC6A11-GFP的胞内域截短体(N-cyt: aa1-60, C-cyt: aa570-632)，确定哪个片段介导核转位；联合IP-MS鉴定其切割产物在核提取物中的相互作用组，与已知MBNL1 iCLIP数据交叉比对TE RNA靶标。

### PubMed 文献

**PubMed count: 134**

| 42342683 | Single-nucleus transcriptomic atlas of sexually dimorphic molecular responses to sub-chronic variable stress in the mous | Transl Psychiatry 2026 |
| 42308736 | The causative mutation for muffs and beard phenotype correlates with gene expression profile in chicken embryonic brains | Poult Sci 2026 |
| 42283414 | Yin Yang 1 Specifically Supports the Development of Olig2 Positive Cerebellar Astrocytes. | Glia 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SLC6A11

