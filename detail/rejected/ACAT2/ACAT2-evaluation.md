---
type: protein-evaluation
gene: "ACAT2"
date: 2026-05-28
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ACAT2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | ACAT2 / Acetyl-CoA acetyltransferase, cytosolic; acetoacetyl-CoA thiolase |
| 蛋白大小 | 397 aa / 41351 Da |
| UniProt ID | Q9BWD1 |
| 评估日期 | 2026-05-28 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 4 /10 | ×3 | 12 | Protein Atlas IF 显示主要定位于胞质溶胶 + 核质 (approved)；UniProt 仅列 cytosol；核定位弱但存在 |
| 📏 蛋白大小 | 10 /10 | ×2 | 20 | 397 aa, 41.4 kDa, 处于理想区间 |
| 🆕 研究新颖性 | 5 /10 | ×3 | 15 | PubMed 260 篇 (1996 年起)；chromatin/epigenetics 仅 66 篇，主要为代谢交叉提及 |
| 🏗️ 三维结构 | 10 /10 | ×3 | 30 | pLDDT 平均 97.2，有序区 99.0%；PAE 均值 3.1 Å，PAE<5 占 88.4%；结构预测质量极佳 |
| 🧬 调控结构域 | 0 /10 | ×2 | 0 | 仅有硫解酶 (thiolase) 结构域，确认为纯代谢酶，无任何染色质/DNA 结合相关结构域 |
| 🔗 PPI ，0% 调控相关 partner |
| ➕ 互证加分 | — | max +3 | 0 | 定位来源矛盾 (IF vs UniProt)；无调控结构域可互证；无调控 PPI 可互证 |
| **原始总分** | | | **77.0 /158** |
| **归一化总分** | | | **48.7 /100** |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| Protein Atlas (IF) | **主要胞质溶胶 (cytosol)** + 核质 (nucleoplasm) | Approved |
| GeneCards | Cytoplasm, cytosol | — |
| UniProt | 细胞质、胞质溶胶、细胞外外泌体 | — |
| GO (CC) | cytoplasm, cytosol, extracellular exosome | — |

![[Projects/TEreg-finding/protein-interested/detail/rejected/ACAT2/IF_images/A431_1.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/rejected/ACAT2/IF_images/U2OS_1.jpg]]

**结论**: Protein Atlas IF 显示 ACAT2 主要定位于胞质溶胶，同时存在核质信号。UniProt 仅注释了胞质定位。核定位证据较弱，但 IF 确实检测到核内信号。得分 4（核+胞质均有分布，无明显偏好，且主要定位于胞质）。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/ACAT2/IF_images/A431_2.jpg|A431_2]]

#### 3.2 蛋白大小评估
**评价**: 397 aa / 41.4 kDa，处于 300-800 aa 理想区间，适合生化纯化和结构解析。硫解酶家族蛋白通常以二聚体形式发挥功能（同源二聚体约 83 kDa）。

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed 总数 | 260 |
| 最早发表年份 | 1996 |
| Chromatin/epigenetics 相关 | 66 (25%) — 几乎全部为代谢综合征/脂代谢中的交叉提及 |

**主要研究方向**:
- 胆固醇/酮体代谢 (acetyl-CoA → acetoacetyl-CoA)
- 脂质代谢疾病
- 癌症代谢重编程 (部分肿瘤中表达上调)
- 代谢酶在细胞增殖中的作用

**评价**: 260 篇文献，研究热点集中在代谢领域。66 篇涉及 chromatin 关键词主要是代谢调控间接关联染色质状态（如乙酰-CoA 作为组蛋白乙酰化底物），非 ACAT2 本身的染色质结合功能。ACAT2 作为染色质调控蛋白的研究完全空白。

#### 3.4 三维结构分析
| 指标 | 数值 |
|---|---|
| AlphaFold 平均 pLDDT | 97.2 |
| PDB 实验结构 | — |
| 有序区域 (pLDDT>70) 占比 | 99.0% (393/397 residues) |
| 高置信度 (pLDDT>90) | 98.0% (389 residues) |
| 低置信度/无序 (pLDDT<50) | 0.8% (3 residues, 均在 N 末端) |
| 可用 PDB 条目 | 未从 GeneCards 检索到实验结构 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/ACAT2/ACAT2-PAE.png]]

**PAE 数值分析**:
- PAE 矩阵尺寸: 397 × 397
- PAE 总体均值: 3.1 Å（预测置信度极高）
- PAE <5 Å 占比: 88.4%（绝大多数残基对定位准确）
- PAE <10 Å 占比: 97.7%
- N/C 半区间 PAE: 3.3 Å（域间关系高度确定）
- 二级结构: α-helix ~35%、β-sheet ~25%、coil ~40%（估计值，典型硫解酶折叠含 α/β 混合结构）

**评价**: ⭐ 结构质量优异。pLDDT 平均值 97.2 是88.4% 的残基对 PAE <5 Å，表明预测结构高度可靠。硫解酶折叠是 α/β 混合结构，含特征性硫解酶 N 端和 C 端结构域。整个蛋白仅有 N 末端的 3 个残基 (0.8%) 处于无序状态。适合基于结构的药物设计和功能研究。

#### 3.5 结构域分析
| 来源 | 结构域 |
|---|---|
| InterPro | Thiolase, N-terminal (IPR020616), Thiolase, C-terminal (IPR020617), Thiolase, active site (IPR020610), Thiolase, conserved site (IPR020613), Thiolase-like superfamily (IPR016039) |
| UniProt | 无额外结构域注释 |

**染色质调控潜力分析**:
- ACAT2 是典型的**硫解酶家族**成员，催化 acetyl-CoA → acetoacetyl-CoA 的可逆反应
- 所有结构域均为**代谢酶催化域**，完全无 DNA/染色质结合结构域
- 蛋白在进化上高度保守（硫解酶折叠从细菌到人类），序列约束来自催化功能而非调控功能
- **结论**: 确认为纯代谢酶，与染色质/DNA 调控无关。得分 0。

> **关联性提示**: 虽然 ACAT2 本身不与染色质结合，但它在胞质中生成的 acetoacetyl-CoA 和消耗的 acetyl-CoA 可间接影响组蛋白乙酰化水平（acetyl-CoA 是组蛋白乙酰转移酶的底物）。这种间接代谢-表观遗传耦合是代谢研究的活跃领域，但属于「代谢调控表观遗传」而非「核蛋白直接调控染色质」。

#### 3.6 PPI :

Top 15 partners:

| Partner | Score | 功能类别 | 与调控相关？ |
|---|---|---|---|
| HMGCS1 | 0.998 | 酮体/胆固醇合成 | 否 |
| HMGCS2 | 0.993 | 酮体合成 (线粒体) | 否 |
| ECI2 | 0.981 | 脂肪酸氧化 | 否 |
| EHHADH | 0.980 | 脂肪酸氧化 | 否 |
| HADHA | 0.974 | 脂肪酸氧化 | 否 |
| OXCT1 | 0.972 | 酮体代谢 | 否 |
| OXCT2 | 0.971 | 酮体代谢 | 否 |
| CS | 0.966 | TCA 循环 | 否 |
| ACOX1 | 0.965 | 脂肪酸氧化 | 否 |
| ACADSB | 0.962 | 脂肪酸氧化 | 否 |
| ACADS | 0.960 | 脂肪酸氧化 | 否 |
| ACACA | 0.959 | 脂肪酸合成 | 否 |
| ACSS2 | 0.959 | 乙酰-CoA 合成 | 否 |
| AACS | 0.958 | 酮体利用 | 否 |
| ACAT1 | 0.950 | 硫解酶 (线粒体) | 否 |

**humanPPI** (prodata.swmed.edu): 详见 STRING API 数据

**PPI 互证**:
- 两工具共同预测的调控相关 neighbor: N/A
- STRING 调控相关比例: **0/30 (0%)**

**调控相关比例**: 0/30 (0%)

**评价**: PPI |

| PPI | STRING only | 纯代谢vs UniProt (cytosol only) | 定位来源矛盾 | ❌ 不一致 |
|---|---|---|---|---|

**互证加分明细**: 无加分项。定位来源矛盾、无调控结构域、无双库 PPI 验证、无实验结构。
- **总分**: **+0 / max +3**

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|---|---|---|---|
| 三维结构 | AlphaFold + PDB | 见 3.4 节 | — |
| 结构域 | UniProt / InterPro / Pfam | 见 3.5 节 | — |
| PPI | STRING | 见 3.6 节 | — |
| 定位 | Protein Atlas IF / UniProt / GO | Nucleus | ✅ |

### 4. 总体评价

**推荐等级**: ⭐ (1/5)

**核心优势**:
1. 三维结构质量极佳 (pLDDT 97.2, PAE 3.1 Å)，适合结构导向研究
2. 蛋白大小理想 (397 aa)，实验操作友好
3. 间接的代谢-表观遗传耦合（acetyl-CoA 作为组蛋白乙酰化底物）

**风险/不确定性**:
1. **本质是代谢酶**：无任何 DNA/染色质结合结构域，所有注释为硫解酶催化域
2. **PPI - AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BWD1
- InterPro: https://www.ebi.ac.uk/interpro/protein/UniProt/Q9BWD1/
- STRING: https://string-db.org/network/9606.ENSP00000356229

![[Projects/TEreg-finding/protein-interested/detail/rejected/ACAT2/ACAT2-PAE.png]]


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/ACAT2/ACAT2-PAE.png]]




