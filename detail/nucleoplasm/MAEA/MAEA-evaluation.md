---
type: protein-evaluation
gene: "MAEA"
date: 2026-06-01
tags: [protein-scout, nucleoplasm, evaluation]
status: scored
---

## MAEA 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | MAEA / EMP |
| 蛋白全名 | E3 ubiquitin-protein transferase MAEA (Macrophage erythroblast attacher) |
| 蛋白大小 | 396 aa / 45.3 kDa |
| UniProt ID | Q7L5Y9 |

### 2. 评分总览
| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | x4 | 32.0 | UniProt: Nucleus nucleoplasm (ECO:0000269 x3); HPA Nucleoplasm (Enhanced) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 396 aa, 45.3 kDa |
| 研究新颖性 | 4/10 | x5 | 20.0 | Strict=66 |
| 三维结构 | 8/10 | x3 | 24.0 | AlphaFold pLDDT 91.5; PDB 8PJN (EM 3.40A); 80.1% >90 |
| 调控结构域 | 7/10 | x2 | 14.0 | CTLH complex E3 ligase subunit; LisH/CTLH domains |
| PPI 网络 | 7/10 | x3 | 21.0 | CTLH complex: ARMC8 (0.986), RMND5A (0.969), WDR26 (0.969) |
| **加权总分** | | | **118/180********** | |
| 互证加分 | | | +2.0 | UniProt + HPA (Enhanced) 一致确认 Nucleoplasm |
| **归一化总分 (÷1.83)** | | | **64.5/100********** | |

PubMed strict: 66

### 3. 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt | Nucleus, nucleoplasm (ECO:0000269 x3); Nucleus matrix (ECO:0000269); Cytoplasm (ECO:0000250); Cell membrane; Cytoskeleton | Experimental |
| GO-CC | nucleoplasm IDA:HPA; nuclear matrix IDA:UniProtKB; nucleus IDA:UniProtKB; GID complex IBA; ubiquitin ligase complex IDA | Direct assay |
| HPA (IF) | Nucleoplasm (main, **Enhanced** 可靠性) | IF available |

**HPA IF 状态**: IF available -- HPA **Enhanced** 级别（最高可靠性等级）。单一定位 Nucleoplasm，无附加胞质信号。Enhanced 可靠性意味着通过 siRNA knockdown 或 GFP 融合蛋白等方式进行了独立验证。

![[MAEA-PAE.png]]

**PAE 状态**: 已获取 PAE 图像。AlphaFold pLDDT 91.5 (mean), 80.1% >90, 仅 1.8% <50。结构质量优异。PDB 8PJN (Cryo-EM 3.40A) 提供了 CTLH complex 的实验结构，MAEA 以全长 1-396 参与复合体。

### 4. PPI 网络
| Partner | Source | Score/Evidence |
|---|---|---|
| ARMC8 | STRING + UniProt | 0.986 (experimental 0.784) |
| RMND5A | STRING + IntAct + UniProt | 0.969 (experimental 0.845) |
| WDR26 | STRING + UniProt | 0.969 (experimental 0.694) |
| GID8 | STRING + UniProt | 0.960 (experimental 0.784) |
| RANBP9 | STRING + UniProt | 0.952 (experimental 0.873) |
| RANBP10 | STRING + UniProt | 0.920 (experimental 0.732) |
| MKLN1 | STRING + UniProt | 0.912 (experimental 0.654) |
| UBE2H | STRING | 0.666 (experimental 0.292) |

**核心发现**: MAEA 是 CTLH (C-terminal to LisH) E3 泛素连接酶复合体的核心催化亚基。CTLH 复合体由 MAEA-RMND5A-WDR26-ARMC8-GID8-RANBP9-RANBP10-MKLN1 等多组分组成，类似于酵母 GID (Glucose-Induced Degradation) 系统。MAEA 与 RMND5A 共同提供催化活性，介导底物蛋白 (如 HBP1) 的泛素化降解。

IntAct 15 条记录。UniProt 记录 8 个互作 partner（均为 CTLH complex 成员）。

**核功能关键线索**: 2025 年 Nature Communications (PMID:41315365) 报道 CTLH complex 底物 ZMYND19 和 MKLN1 负调控 mTORC1 在溶酶体膜上的活性，而 MAEA 本身定位于 nucleoplasm 和 nuclear matrix，提示 CTLH complex 可能在核内外具有时空分离的功能模块。

### 5. 结构域与染色质调控潜力
| 来源 | 结构域 |
|---|---|
| InterPro | IPR013144 (CTLH/CRA), IPR006595 (CTLH C-term LisH), IPR006594 (LisH), IPR045098 (MAEA-like), IPR044063 (MAEA CTLH) |
| Pfam | PF10607 (CTLH) |

MAEA 包含 LisH (Lissencephaly type-1-like homology) 和 CTLH (C-terminal to LisH) 结构域，这些结构域在多种 E3 泛素连接酶复合体中充当 scaffold。Nuclear matrix 定位 (IDA:UniProtKB) 提示 MAEA 与核骨架关联，可能参与核内蛋白质质量控制或转录因子（如 HBP1）的泛素化降解调控。

**染色质调控潜力**: 通过 CTLH complex 泛素化降解转录因子间接参与基因表达调控。无直接 DNA/chromatin binding 结构域，属于 "泛素化介导的间接染色质调控" 类别。

### 6. 总体评价
MAEA 是本研究核定位证据最强的蛋白之一：UniProt 实验级别 nucleoplasm (ECO:0000269 x3) + HPA Enhanced + GO-CC IDA:HPA/IDA:UniProtKB 三重确认。CTLH complex 的 E3 连接酶催化亚基，PPI 网络以复合体成员为主且置信度高。结构质量优异 (pLDDT 91.5 + PDB 8PJN)。主要劣势是 PubMed 66（新颖性中等）。适合作为核内泛素化-转录调控交叉方向的中高优先级靶点。

**推荐等级**: 3.5/5

**HPA IF 状态**: HPA IF 图像已本地嵌入。

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MAEA/IF_images/MAEA_IF_407_D2_1_red_green.jpg]]。核定位基于HPA localization/reliability + UniProt + GO-CC。


![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MAEA/MAEA-PAE.png]]


#### 关键文献
| PMID | 标题 |
|---|---|
| 34182925 | The plasma peptides of Alzheimer's disease. |
| 35342354 | TBC1D14 inhibits autophagy to suppress lymph node metastasis in head and neck squamous cell carcinom |
| 36444483 | maea affects head formation through ß-catenin degradation during early Xenopus laevis development. |
| 41524512 | Dysregulation of U12-Type Splicing in Lupus Neutrophils. |
| 31795790 | The GID ubiquitin ligase complex is a regulator of AMPK activity and organismal lifespan. |

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MAEA/MAEA-PAE.png]]
