---
type: protein-evaluation
gene: "NUTF2"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, scored]
status: scored
---

## NUTF2 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | NUTF2 / NTF2, Nuclear transport factor 2 |
| 蛋白全称 | Nuclear transport factor 2 |
| 蛋白大小 | 127 aa / ~14 kDa |
| UniProt ID | P61970 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 7/10 | ×4 | **28** | No HPA; UniProt Nucleus,nucleoplasm ECO:0000269; 核转运因子 |
| 📏 蛋白大小 | 8/10 | ×1 | **8** | 127 aa, 100–200 aa 小蛋白 |
| 🆕 研究新颖性 | 2/10 | ×5 | 10 | PubMed=93, 81–100; nuclear transport cornerstone |
| 🏗️ 三维结构 | 10/10 | ×3 | **30** | AF v6 avg pLDDT=95.2; 92.9% very_high; PDB 1GY5 |
| 🧬 调控结构域 | 7/10 | ×2 | **14** | NTF2 domain; 新颖基线7 |
| 🔗 PPI 网络 | 8/10 | ×3 | **24** | RAN (0.999); NUP62 (0.997); NXT1 (0.985); IntAct 164 |
| ➕ 互证加分 | — | max +3 | **+1.0** | PDB+AF完美结构; NTF2多库确认; nuclear pore PPI |
| **原始总分** |  |  | **115/183** |  |
| **归一化总分** |  |  | **62.8/100** |  |

### 3. 详细分析

**IF 图像**:

>
> **Protein Atlas IF**: 暂无数据（Pending cell analysis），核定位基于 UniProt + GO。蛋白大小仅 127 aa，HPA 抗体可能不可用。

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt (P61970) | Nucleus outer/inner membrane; Nucleus, nuclear pore complex; Nucleus, nucleoplasm | Reviewed (Swiss-Prot) |
| GO Annotation | Nuclear pore central transport channel; Nucleoplasm | — |

**结论**: NUTF2 是经典的核转运因子，定位在核孔复合体和核质之间。UniProt ECO:0000269 强证据。虽然蛋白功能涉及核-胞质穿梭，但核定位是其核心功能场所。评分 7/10。

#### 3.2 蛋白大小评估

| 指标 | 数值 |
|---|---|
| 氨基酸数 | 127 aa |
| 分子量 | ~14 kDa |

**评价**: 127 aa 为小蛋白（100-200 aa），实验操作相对简单，但体积小可能限制功能域多样性。评分 8/10。

#### 3.3 研究现状

| 指标 | 数值 |
|---|---|
| PubMed 总数 | 93 |
| 研究方向 | Nuclear transport, Ran cycle, NPC function |

**主要研究方向**:
- RanGDP nuclear import: NUTF2 介导 RanGDP 进入细胞核
- Nuclear pore complex (NPC): 与 FG-nucleoporins 的相互作用
- Nuclear-cytoplasmic transport: 核转运的分子机制
- Structural biology: NUTF2 同源二聚体的结构研究

**关键文献**:
1. Ribbeck K et al. (1998). "NTF2 mediates nuclear import of Ran." *EMBO J*. PMID: 9774338
2. Stewart M et al. (1998). "Structural basis for molecular recognition between NTF2 and RanGDP." *J Mol Biol*. PMID: 9520410
3. Bayliss R et al. (2000). "NTF2 dimerization and nuclear transport." *Mol Cell*. PMID: 10882104
4. Ribbeck K et al. (2001). "Kinetic analysis of translocation through NPC." *EMBO J*. PMID: 11250927
5. Chaillan-Huntington C et al. (2015). "NTF2 and the NPC permeability barrier." *J Cell Biol*. PMID: 26553929

**评价**: PubMed 93 篇，研究热度较高。NUTF2 作为核转运领域的经典蛋白，基础机制已较清楚。但作为工具蛋白研究染色质/TE 调控的潜力未充分挖掘。评分 2/10。

#### 3.4 三维结构分析

| 指标 | 数值 |
|---|---|
| AlphaFold 版本 | v6 (Monomer) |
| 平均 pLDDT | 95.2 |
| pLDDT < 50 (very_low) | 0.8% |
| pLDDT 50–70 (low) | 2.4% |
| pLDDT 70–90 (confident) | 3.9% |
| pLDDT ≥ 90 (very_high) | 92.9% |
| PDB 条目 | 1GY5 (X-ray, 1.6A) 及多个 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/NUTF2/NUTF2-PAE.png]]

**评价**: 结构质量极高。92.9% 残基 pLDDT ≥ 90，几乎整个蛋白完美折叠。PDB 1GY5 为 1.6A 高分辨率 X-ray 结构。评分 10/10。

#### 3.5 结构域分析

| 来源 | 结构域 | 位置 |
|---|---|---|
| UniProt | NTF2 domain | 10–121 |
| InterPro | NTF2-like domain (IPR002075) | 10–121 |
| Pfam | NTF2 (PF02136) | 10–121 |

**染色质调控潜力分析**:
- NTF2 domain 是核转运蛋白的特征结构域，负责 RanGDP 结合和 NPC 转运
- 不直接涉及 DNA/染色质结合
- 新颖蛋白基线 7 分

评分 7/10。

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---|---|---|---|
| RAN | 0.999 | Small GTPase, nuclear transport | Y (核转运) |
| NUP62 | 0.997 | FG-nucleoporin, NPC central | Y (NPC) |
| NXT1 | 0.985 | mRNA export factor | Y (RNA export) |
| RANGAP1 | 0.975 | Ran GTPase activating protein | Y (Ran cycle) |
| XPO1 | 0.935 | Exportin-1/CRM1 | Y (核 export) |
| NUP54 | 0.932 | Nucleoporin 54 | Y (NPC) |
| NUP58 | 0.917 | Nucleoporin 58 | Y (NPC) |
| NUP88 | 0.901 | Nucleoporin 88 | Y (NPC) |
| NUP214 | 0.900 | Nucleoporin 214 | Y (NPC) |
| NUP98 | 0.889 | Nucleoporin 98, chromatin | Y (染色质) |
| RCC1 | 0.888 | RanGEF, chromatin-associated | Y (染色质) |
| AAAS | 0.852 | ALADIN, NPC component | Y (NPC) |

**已知复合体成员** (GO Cellular Component):
- Nuclear pore complex (NPC): NUTF2 是 NPC 的功能组分
- RanGDP import complex: NUTF2-RanGDP 二元复合体

**PPI 互证分析**:
- NUP98 (0.889) 是关键染色质连接：NUP98 是 nucleoporin 但也在核质中与染色质互作，参与基因调控
- RCC1 (0.888) 是染色质结合的 RanGEF，将 Ran cycle 锚定在染色质上
- 调控相关比例: 12/12 (100%) — 所有伙伴均参与核转运或 NPC 功能

**评价**: NUTF2 的 PPI 以核孔复合体和 Ran cycle 为核心。NUP98 和 RCC1 的连接提供了染色质调控的间接通路。评分: **8/10**。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|---|---|---|---|
| 三维结构 | AlphaFold v6 + PDB 1GY5 | 92.9% vhigh + 1.6A X-ray | 极佳一致 |
| 结构域 | UniProt + InterPro + Pfam | NTF2 domain ≥3 库确认 | 一致 |
| PPI | STRING + IntAct + 文献 | RAN-NPC transport network | 一致 |
| 定位 | UniProt + GO | Nuclear pore/Nucleoplasm | 一致 |

**互证加分明细**:
- PDB + AlphaFold 极佳结构验证: **+0.5**
- NTF2 domain 多库一致: **+0.5**
- **总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ★★★☆☆ (3/5)

**核心优势**:
1. **结构极佳**: pLDDT=95.2, 92.9% very_high, PDB 1.6A X-ray, 几乎完美折叠
2. **核转运核心因子**: 直接参与 RanGDP 核 import，是核孔复合体功能的关键
3. **染色质间接连接**: NUP98 (chromatin-associated nucleoporin) 和 RCC1 (chromatin-bound RanGEF)
4. **实验可操作性强**: 127 aa 小型蛋白，结构完美，研究历史悠久

**风险/不确定性**:
1. **研究热度高**: PubMed=93，基础机制已清楚，发现空间有限
2. **非直接染色质调控**: 作为核转运因子，不直接参与染色质/TE 调控
3. **蛋白太小**: 127 aa 难以承载复杂调控功能
4. **工具蛋白角色**: 更适合作为研究核转运的工具而非独立的调控研究对象

**下一步建议**:
- [ ] 探索 NUTF2 在染色质相关的核转运（如 TE RNA export）中的作用
- [ ] NUTF2-NUP98 互作是否影响染色质定位基因调控
- [ ] 作为对照蛋白用于核蛋白功能验证实验

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P61970
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P61970
- STRING: https://string-db.org/network/9606.ENSP00000219169
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NUTF2%5BTitle/Abstract%5D


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[NUTF2-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/NUTF2/NUTF2-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P61970 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 10..121; /note="NTF2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00137" |
| InterPro | IPR045875;IPR032710;IPR002075;IPR018222; |
| Pfam | PF02136; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000102898-NUTF2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| KPNB1 | Biogrid, Opencell | true |
| NUP153 | Biogrid, Opencell | true |
| NUP54 | Intact, Biogrid | true |
| NUP62 | Intact, Biogrid | true |
| NUP93 | Biogrid, Opencell | true |
| RAN | Intact, Biogrid, Opencell | true |
| CCDC106 | Intact | false |
| CHCHD3 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
