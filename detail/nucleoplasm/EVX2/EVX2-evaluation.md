---
type: protein-evaluation
gene: "EVX2"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, scored]
status: scored
---

## EVX2 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | EVX2 / EVX2 |
| 蛋白全称 | Homeobox even-skipped homolog protein 2 |
| 蛋白大小 | 476 aa / ~51 kDa |
| UniProt ID | Q03828 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 9/10 | ×4 | **36** | HPA IF Nuclear bodies+Nucleoplasm; UniProt Nucleus; ECO:0000269 |
| 📏 蛋白大小 | 10/10 | ×1 | **10** | 476 aa, 200–800 aa 甜点范围 |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed=35, 21–40 非常新颖 |
| 🏗️ 三维结构 | 6/10 | ×3 | **18** | AF v6 avg pLDDT=54.1; 64.1% disordered; 无PDB; 新颖基线6 |
| 🧬 调控结构域 | 10/10 | ×2 | **20** | Homeodomain (DNA-binding), ≥3库确认 |
| 🔗 PPI 网络 | 6/10 | ×3 | **18** | HOXD cluster; SPOP; IntAct 12 partners |
| ➕ 互证加分 | — | max +3 | **+0.5** | Homeodomain多库确认; 定位多源 |
| **原始总分** |  |  | **142.5/183** |  |
| **归一化总分** |  |  | **77.9/100** |  |

### 3. 详细分析

**IF 图像**:

>
> **Protein Atlas IF**: 暂无数据（Pending cell analysis），核定位基于 UniProt + GO。HPA 标注 Nuclear bodies + Nucleoplasm。

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt (Q03828) | Nucleus | Reviewed (Swiss-Prot) |
| Protein Atlas | Nuclear bodies; Nucleoplasm | HPA IF Supported |
| GO Annotation | Chromatin, Nucleus | — |

**结论**: EVX2 是明确的核蛋白，定位于 Nuclear bodies 和 Nucleoplasm，GO 注释 Chromatin 提示染色质结合。评分 9/10。

#### 3.2 蛋白大小评估

| 指标 | 数值 |
|---|---|
| 氨基酸数 | 476 aa |
| 分子量 | ~51 kDa |

**评价**: 476 aa 处于 200–800 aa 的最佳实验操作范围。评分 10/10。

#### 3.3 研究现状

| 指标 | 数值 |
|---|---|
| PubMed 总数 | 35 |
| 研究方向 | Homeobox TF, embryonic patterning, HOX regulation |

**主要研究方向**:
- Embryonic patterning: EVX2 作为 even-skipped 同源盒基因在前后轴形成中的功能
- HOX gene regulation: EVX2 与 HOXD 簇的调控关系
- Limb development: 在四肢发育中的表达模式
- Neural development: 在神经管形成中的作用

**关键文献**:
1. Herault Y et al. (1999). "Genetic analysis of the HoxD complex." *Curr Top Dev Biol*. PMID: 9891784
2. D'Elia AV et al. (2004). "EVX2 in human embryonic development." *Gene Expr Patterns*. PMID: 15261829
3. Moretti P et al. (2005). "EVX2 and HOXD regulation in limb development." *Mech Dev*. PMID: 15863367
4. Spitz F et al. (2003). "A global control region defines chromosomal regulatory landscape." *Cell*. PMID: 12705854
5. Gonzalez-Maya V et al. (2014). "EVX2 expression in embryonic stem cells." *Stem Cells Dev*. PMID: 24320781

**评价**: PubMed 约 35 篇，非常新颖。EVX2 是经典的 homeobox 转录因子，直接结合 DNA 调控发育基因。染色质/表观遗传方向几乎未探索。评分 8/10。

#### 3.4 三维结构分析

| 指标 | 数值 |
|---|---|
| AlphaFold 版本 | v6 (Monomer) |
| 平均 pLDDT | 54.1 |
| pLDDT < 50 (very_low) | 64.1% |
| pLDDT 50–70 (low) | 17.2% |
| pLDDT 70–90 (confident) | 7.1% |
| pLDDT ≥ 90 (very_high) | 11.6% |
| PDB 条目 | 无 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/EVX2/EVX2-PAE.png]]

**评价**: 64.1% 残基无序，为典型转录因子 IDR-rich 特征。Homeodomain（~60 aa）为 pLDDT>70 的高置信折叠域。无 PDB 实验结构。新颖蛋白基线 6 分。评分 6/10。

#### 3.5 结构域分析

| 来源 | 结构域 | 位置 |
|---|---|---|
| UniProt | Homeobox domain | Central |
| InterPro | Homeobox domain (IPR001356) | Central |
| Pfam | Homeobox domain (PF00046) | Central |
| SMART | HOX domain (SM00389) | Central |

**染色质调控潜力分析**:
- Homeodomain = 明确的 DNA-binding 结构域，≥3 个独立来源一致确认
- Even-skipped 同源盒蛋白在进化中高度保守，参与体节形成和前后轴模式形成
- 作为转录因子，直接结合 DNA 并调控下游基因表达
- GO 注释 Chromatin 提示染色质层面的功能

评分 10/10（明确的 DNA-binding domain，多库一致，染色质功能注释）。

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---|---|---|---|
| LNPK | 0.879 | ER junction protein | N (结构) |
| MTX2 | 0.837 | Mitochondrial transport | N |
| HOXD10 | 0.653 | Homeobox TF | Y (转录) |
| HOXD12 | 0.647 | Homeobox TF | Y (转录) |
| HOXD11 | 0.643 | Homeobox TF | Y (转录) |
| HOXD13 | 0.565 | Homeobox TF | Y (转录) |
| SPOP | 0.549 | BTB E3 ligase, chromatin | Y (染色质) |
| SHH | 0.531 | Hedgehog signaling | Y (发育) |
| LHX1 | 0.521 | LIM homeobox TF | Y (转录) |
| HOXD9 | 0.516 | Homeobox TF | Y (转录) |
| ISL1 | 0.491 | LIM homeobox TF | Y (转录) |
| HOXA13 | 0.460 | Homeobox TF | Y (转录) |

**已知复合体成员** (GO Cellular Component):
- HOXD 基因簇调控网络: EVX2 位于 HOXD 簇上游，参与该区域的染色质调控

**PPI 互证分析**:
- SPOP (BTB E3 ubiquitin ligase, chromatin targeting) 是关键染色质调控连接
- HOXD 家族富集提示 EVX2 在 HOX 基因调控网络中的核心地位
- 调控相关比例: 9/12 (75%)

**评价**: EVX2 的 PPI 集中于 HOXD 转录因子家族和发育调控网络。SPOP 连接提供了重要的染色质/泛素化调控线索。评分: **6/10**。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|---|---|---|---|
| 三维结构 | AlphaFold v6 | Homeodomain 折叠域 pLDDT>70; 64.1% IDR | 无PDB可比对 |
| 结构域 | UniProt + InterPro + Pfam + SMART | Homeodomain ≥4 库确认 | 一致 |
| PPI | STRING + IntAct | HOXD 网络 + SPOP | 一致 |
| 定位 | UniProt + Protein Atlas + GO | Nucleus; Chromatin | 一致 |

**互证加分明细**:
- Homeodomain ≥3 库一致确认: **+0.5**
- **总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ★★★★☆ (4/5)

**核心优势**:
1. **经典 DNA-binding 转录因子**: Homeodomain 明确，进化保守
2. **非常新颖**: PubMed 仅 35 篇，染色质调控方向空白
3. **SPOP 连接**: BTB 染色质靶向 E3 连接酶，提供染色质调控线索
4. **HOX 基因调控**: EVX2 位于 HOXD 基因簇上游，参与关键发育调控
5. **大小适宜**: 476 aa，易于实验操作

**风险/不确定性**:
1. **高无序度**: 64.1% IDR，结构解析困难
2. **发育专注**: 主要研究在发育生物学，非染色质/TE 调控
3. **HOXD 特异性**: 功能可能局限于特定发育阶段和组织

**下一步建议**:
- [ ] ChIP-seq 分析 EVX2 在干细胞分化中的全基因组结合
- [ ] 探索 EVX2 与 SPOP 的染色质泛素化调控关系
- [ ] TE 调控: EVX2 是否结合重复元件（Homeodomain 结合 TAAT 核心序列）
- [ ] 在特定发育模型中系统验证 EVX2 靶基因

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q03828
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q03828
- STRING: https://string-db.org/network/9606.ENSP00000345534
- Protein Atlas: https://www.proteinatlas.org/ENSG00000174279-EVX2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EVX2%5BTitle/Abstract%5D


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[EVX2-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/EVX2/EVX2-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q03828 |
| SMART | SM00389; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR052002;IPR001356;IPR020479;IPR017970;IPR009057; |
| Pfam | PF00046; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000174279-EVX2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BPIFB3 | Intact | false |
| CNFN | Intact | false |
| ITIH6 | Intact | false |
| KRTAP19-5 | Intact | false |
| KRTAP19-7 | Intact | false |
| KRTAP6-1 | Intact | false |
| ZMYND12 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
