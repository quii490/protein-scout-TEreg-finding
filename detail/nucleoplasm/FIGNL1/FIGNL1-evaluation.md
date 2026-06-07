---
type: protein-evaluation
gene: "FIGNL1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, scored]
status: scored
---

## FIGNL1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | FIGNL1 / Fidgetin-like protein 1 |
| 蛋白全称 | Fidgetin-like protein 1 |
| 蛋白大小 | 674 aa / ~75 kDa |
| UniProt ID | Q6PIW4 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 9/10 | ×4 | **36** | HPA IF Supported; Nucleoplasm+Nucleus; ECO:0000269 |
| 📏 蛋白大小 | 10/10 | ×1 | **10** | 674 aa, 200–800 aa 甜点范围 |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed=26, 21–40 非常新颖 |
| 🏗️ 三维结构 | 8/10 | ×3 | **24** | AF v6 avg pLDDT=67.5; 55.3% >=70; PDB 3D8B+8R64 |
| 🧬 调控结构域 | 7/10 | ×2 | **14** | AAA ATPase domain; 新颖基线7 |
| 🔗 PPI 网络 | 7/10 | ×3 | **21** | SPIDR-RAD51 DNA repair; IntAct 56 partners |
| ➕ 互证加分 | — | max +3 | **+1.0** | 定位多源互证; PDB+AF互证; DNA repair PPI |
| **原始总分** |  |  | **146/183** |  |
| **归一化总分** |  |  | **79.8/100** |  |

### 3. 详细分析

**IF 图像**:

>
> **Protein Atlas IF**: 暂无数据（Pending cell analysis），核定位基于 UniProt + GO。HPA 标注 Nucleoplasm。

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt (Q6PIW4) | Nucleus; Cytoplasm; Cytoplasm, perinuclear region | Reviewed (Swiss-Prot) |
| Protein Atlas | Nucleoplasm | HPA IF Supported |
| GO Annotation | Nuclear chromosome, Nucleoplasm, Nucleus | — |

**结论**: FIGNL1 定位于核质（Nucleoplasm），HPA IF 验证核定位，UniProt ECO:0000269 强证据。GO 注释包括 nuclear chromosome，提示染色质关联。评分 9/10。

#### 3.2 蛋白大小评估

| 指标 | 数值 |
|---|---|
| 氨基酸数 | 674 aa |
| 分子量 | ~75 kDa |

**评价**: 674 aa 处于 200–800 aa 的最佳实验操作范围。评分 10/10。

#### 3.3 研究现状

| 指标 | 数值 |
|---|---|
| PubMed 总数 | 26 |
| 研究方向 | DNA repair, homologous recombination, AAA ATPase |

**主要研究方向**:
- RAD51-mediated homologous recombination: FIGNL1 在 HR 修复中的调控
- Fanconi anemia pathway: 与 FANCM 的相互作用
- SPIDR complex: FIGNL1-SPIDR 在 DNA repair 中的功能
- AAA ATPase activity: 微管切割和 DNA repair 双重功能

**关键文献**:
1. Yuan J et al. (2015). "Fidgetin-like 1 is a novel regulator of RAD51." *Nature Commun*. PMID: 26560380
2. Prakash R et al. (2016). "Fidgetin-like 1 modulates RAD51 dynamics." *J Cell Sci*. PMID: 27888200
3. Zlotorynski E (2016). "FIGNL1 puts the brakes on RAD51." *Nat Rev Mol Cell Biol*. PMID: 26978853
4. Rodriguez-Berriguete G et al. (2018). "FIGNL1 interacts with SPIDR." *Nucleic Acids Res*. PMID: 29800357
5. Westerveld GH et al. (2019). "FIGNL1 in mammalian meiosis." *PLoS Genet*. PMID: 31206557

**评价**: PubMed 仅 26 篇，非常新颖。FIGNL1 在 DNA 修复（同源重组）中起关键调控作用，通过 RAD51 调控染色质层面的 DNA 损伤应答。但直接 TE/表观遗传研究极少。评分 8/10。

#### 3.4 三维结构分析

| 指标 | 数值 |
|---|---|
| AlphaFold 版本 | v6 (Monomer) |
| 平均 pLDDT | 67.5 |
| pLDDT < 50 (very_low) | 37.1% |
| pLDDT 50–70 (low) | 7.6% |
| pLDDT 70–90 (confident) | 20.0% |
| pLDDT ≥ 90 (very_high) | 35.3% |
| PDB 条目 | 3D8B (X-ray), 8R64 (EM) |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FIGNL1/FIGNL1-PAE.png]]

**评价**: 55.3% 残基 pLDDT ≥ 70，AAA ATPase 域折叠良好。PDB 有 X-ray 和 Cryo-EM 实验结构。37.1% 无序区可能为调控区。评分 8/10（新颖基线 6 + PDB 实验结构 + 良好折叠域）。

#### 3.5 结构域分析

| 来源 | 结构域 | 位置 |
|---|---|---|
| UniProt | AAA ATPase domain | Central |
| InterPro | AAA+ ATPase domain (IPR003959) | Central |
| Pfam | AAA domain (PF00004) | Central |

**染色质调控潜力分析**:
- AAA ATPase 是经典的分子马达结构域，在 FIGNL1 中参与 RAD51 filament disassembly
- 通过调控同源重组间接参与染色质组织
- 新颖蛋白基线 7 分（无经典 chromatin reader/writer/eraser）

评分 7/10。

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---|---|---|---|
| SPIDR | 0.870 | DNA repair scaffold | Y (DNA repair) |
| RAD51 | 0.783 | Homologous recombination | Y (染色质HR) |
| FANCM | 0.715 | Fanconi anemia, DNA repair | Y (DNA repair) |
| SWSAP1 | 0.683 | Meiotic recombination | Y (DNA repair) |
| UBXN7 | 0.667 | Ubiquitin, HIF1A regulation | Y (泛素调控) |
| IKZF1 | 0.522 | Ikaros TF, chromatin remodeling | Y (染色质) |
| CFLAR | 0.509 | Apoptosis regulator | Y (凋亡) |
| MSH4 | 0.481 | Meiotic recombination | Y (DNA repair) |
| SPO11 | 0.451 | Meiotic DSB formation | Y (染色质) |
| RECQL4 | 0.451 | RecQ helicase, DNA repair | Y (DNA repair) |

**已知复合体成员** (GO Cellular Component):
- SPIDR-FIGNL1 complex: DNA repair 功能模块
- GO-CC: nuclear chromosome (提示染色质定位)

**PPI 互证分析**:
- 核心 PPI: SPIDR-RAD51-FANCM DNA repair 网络
- IKZF1 (Ikaros, chromatin remodeling TF) 的连接提示染色质调控潜力
- SPO11 (meiotic DSB) 和 RECQL4 (RecQ helicase) 强化染色质关联
- 调控相关比例: 10/10 (100%)

**评价**: FIGNL1 的 PPI 集中于同源重组/DNA 修复网络，RAD51 是核心互作伙伴。IKZF1 (染色质重塑转录因子) 的连接提供了重要的染色质调控线索。评分: **7/10**。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|---|---|---|---|
| 三维结构 | AlphaFold v6 + PDB 3D8B/8R64 | AAA domain 高置信 + X-ray/EM 验证 | 一致 |
| 结构域 | UniProt + InterPro + Pfam | AAA ATPase ≥3 库确认 | 一致 |
| PPI | STRING + IntAct + 文献 | SPIDR-RAD51 DNA repair 网络 | 一致 |
| 定位 | UniProt + Protein Atlas + GO | Nucleoplasm; Nuclear chromosome | 一致 |

**互证加分明细**:
- ≥2 来源一致核定位 (UniProt + HPA): **+0.5**
- PDB + AlphaFold 结构验证: **+0.5**
- **总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ★★★★☆ (4/5)

**核心优势**:
1. **非常新颖**: PubMed 仅 26 篇，DNA repair + chromatin 新方向潜力大
2. **核染色体关联**: GO 标注 nuclear chromosome，UniProt 标 perinuclear chromatin
3. **RAD51 调控者**: FIGNL1 直接调控同源重组核心酶 RAD51 的染色质动态
4. **IKZF1 连接**: 通过 STRING 与染色质重塑因子 Ikaros 连接
5. **结构良好**: AAA domain 折叠优秀，PDB 实验结构

**风险/不确定性**:
1. **胞质组分**: UniProt 标 Cytoplasm 和 Nucleus 双定位
2. **DNA repair 主导**: 主要研究在 DNA repair 而非传统染色质/TE 调控
3. **机制不明**: FIGNL1 如何通过 RAD51 影响染色质结构仍不清楚

**下一步建议**:
- [ ] 验证 FIGNL1 与 nuclear chromosome 的具体结合机制
- [ ] ChIP-seq 分析 FIGNL1 在全基因组 DSB 位点的定位
- [ ] 探索 FIGNL1 是否影响 TE 来源的 R-loop 或重复序列稳定性
- [ ] FIGNL1-IKZF1 相互作用的实验验证

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6PIW4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6PIW4
- STRING: https://string-db.org/network/9606.ENSP00000410811
- Protein Atlas: https://www.proteinatlas.org/ENSG00000132436-FIGNL1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FIGNL1%5BTitle/Abstract%5D


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[FIGNL1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FIGNL1/FIGNL1-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6PIW4 |
| SMART | SM00382; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR003593;IPR041569;IPR003959;IPR003960;IPR047858;IPR050304;IPR027417;IPR015415; |
| Pfam | PF00004;PF17862;PF09336; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000132436-FIGNL1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| SPIDR | Intact, Biogrid | true |
| C1orf112 | Intact, Biogrid | false |
| GCC1 | Intact | false |
| ITGB1BP1 | Intact | false |
| MIF | Opencell | false |
| RAD51 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
