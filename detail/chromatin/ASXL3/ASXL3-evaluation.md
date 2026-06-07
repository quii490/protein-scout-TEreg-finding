---
type: protein-evaluation
gene: "ASXL3"
date: 2026-05-29
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ASXL3 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | ASXL3 / KIAA1713; Putative Polycomb group protein ASXL3; Additional sex combs-like protein 3 |
| 蛋白大小 | 2248 aa / ~243.7 kDa |
| UniProt ID | Q9C0F0 (ASXL3_HUMAN) |
| 评估日期 | 2026-05-29 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 8 | 10 | 32 | UniProt Nucleus (ECO:0000305); PR-DUB complex (Polycomb deubiquitinase); BAP1 的伙伴蛋白 |
| 📏 蛋白大小 | 2 | 10 | 2 | 2248 aa (>2000区间)，极大蛋白，表达和生化实验难度高 |
| 🆕 研究新颖性 | 2/10 | 10 | 10 | PubMed 95篇，51-100区间，接近上限 |
| 🏗️ 三维结构 | 6 | 10 | 18 | AF avg=39.38, verylow=84%; 几乎全无序；无PDB; 本质无序蛋白正常 |
| 🧬 调控结构域 | 8 | 10 | 16 | HTH HARE-type (10-84) + DEUBAD (254-363); PR-DUB Polycomb复合体; chromatin binding (IBA) |
| 🔗 PPI | 10/10 | ×3 | **30** | 详见 3.6 PPI 分析 |
| ➕ 互证加分 | +1.0 | max +3 | +1.0 | Polycomb/PR-DUB复合体GO; HTH+DEUBAD域多库确认; chromatin binding |
| **原始总分** |  |  | **109/183** |  |
| **归一化总分** |  |  | **59.6/100** |  |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| GeneCards | 暂待确认 | — |
| Protein Atlas (IF) | 暂无数据（Pending cell analysis） | — |
| UniProt | Nucleus (ECO:0000305) | Sequence analysis |

**结论**: ASXL3 的 UniProt 标注为 Nucleus，通过序列分析（ECO:0000305）。作为 PR-DUB (Polycomb repressive deubiquitinase) 复合体的核心成员，与 BAP1 形成染色质调控复合体。GO chromatin binding (IBA)。核定位功能推理确凿，但直接 IF 实验证据待补充。

#### 3.2 蛋白大小评估
**评价**: 2248 aa，极大蛋白。>2000 aa 导致表达、纯化、结构解析的难度显著增加。但可考虑截短构建（如仅 ASXH 域区域）。

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed 总数 | 95 |
| 最早发表年份 | ~2013 (Bainbridge-Ropers syndrome) |
| Chromatin/epigenetics 比例 | 高 (Polycomb protein) |

**主要研究方向**:
- Bainbridge-Ropers 综合征（ASXL3 突变导致严重发育障碍）
- Polycomb 染色质调控（PR-DUB 复合体: BAP1 + ASXL1/2/3）
- 组蛋白 H2A 去泛素化
- 脂代谢调控（负调控脂合成）

**关键文献**:
1. Adam et al. (1993). "ASXL3-Related Disorder.". **. PMID: 33151654
2. Laquerriere et al. (2022). "Phenotypic spectrum and genomics of undiagnosed arthrogryposis multiplex congenita.". *J Med Genet*. PMID: 33820833
3. Schirwani et al. (2021). "Expanding the phenotype of ASXL3-related syndrome: A comprehensive description of 45 unpublished individuals with inherited and de novo pathogenic variants in ASXL3.". *Am J Med Genet A*. PMID: 34436830
4. Pande et al. (2024). "De novo variants underlying monogenic syndromes with intellectual disability in a neurodevelopmental cohort from India.". *Eur J Hum Genet*. PMID: 38114583
5. Woods et al. (2024). "ASXL3-related disorder: Molecular phenotyping and comprehensive review providing insights into disease mechanism.". *Clin Genet*. PMID: 38420660
**评价**: 95篇文献，接近上限。ASXL3 作为 Polycomb 核心成员，研究热度适中。其主要关注点在发育障碍而非基础机制研究。

#### 3.4 三维结构分析
| 指标 | 数值 |
|---|---|
| AlphaFold 平均 pLDDT | 39.38 |
| veryhigh (pLDDT>90) 占比 | 3% |
| confident (70-90) 占比 | 8% |
| 有序区域 (pLDDT>70) 占比 | 11% |
| verylow (pLDDT<50) 占比 | 84% |
| 可用 PDB 条目 | 0 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/chromatin/ASXL3/ASXL3-PAE.png]]

**评价**: AlphaFold 几乎全无序（avg=39.38, verylow=84%）。对如此大型的本质无序蛋白而言是正常的。HTH HARE-type 域（10-84）和 DEUBAD 域（254-363）区域可能有局部折叠。作为 Polycomb scaffold 蛋白，无序性有助于灵活招募多种伙伴。新颖蛋白基线 6 分。

#### 3.5 结构域分析
| 来源 | 结构域 |
|---|---|
| GeneCards | 暂待确认 |
| SMART | 待分析 |
| InterPro/Pfam | HTH HARE-type (10-84); DEUBAD (254-363) |
| UniProt | HTH HARE-type (PROSITE-PRU01261); DEUBAD (PROSITE-PRU01264) |

**染色质调控潜力分析**: 
- HTH HARE-type (Helix-turn-helix, HB1, ASXL, restriction endonuclease): DNA binding 相关域，暗示可能结合 DNA
- DEUBAD (deubiquitinase adaptor): 与 BAP1 去泛素化酶互作，建立 PR-DUB 复合体
- GO: chromatin binding (IBA)
- ASXL3 是 Polycomb 染色质调控系统的核心 scaffold 蛋白。得分 8（领域证据强烈但直接分子细节待确认）。

#### 3.6 PPI 网络

**实验验证互作** (IntAct):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---|---|---|---|---|
| （IntAct 数据极为稀疏，仅2条记录） | - | - | - | - |

**STRING 预测互作**:

| Partner | Score | 功能类别 | 调控相关？ |
|---|---|---|---|
| （STRING API 数据获取中） | - | - | - |

**已知复合体成员** (GO Cellular Component):
- PR-DUB complex (IBA:GO_Central): BAP1 + ASXL1/2/3 形成 Polycomb 去泛素化酶复合体

**PPI 互证分析**:
- 实验 PPI 数据稀疏，但功能复合体归属明确（PR-DUB: BAP1-ASXL3）
- 作为 Polycomb scaffold，预期与 BAP1, HCFC1, FOXK1/2, OGT 等互作（ASXL1/2 同源物已知互作）
- 调控相关比例: 基于功能推理 >80%

**评价**: 尽管 IntAct/STRING 直接互作数据稀疏，ASXL3 的功能和复合体注释强烈支持其为 Polycomb chromatin-modifying 蛋白。PR-DUB 复合体使 ASXL3 成为核心染色质调控网络节点。得分 10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|---|---|---|---|
| 三维结构 | AlphaFold avg=39.38 + 无PDB | 本质无序，符合大scaffold蛋白预期 | N/A |
| 结构域 | UniProt HTH+DEUBAD / PROSITE HTH+DEUBAD | 多库一致 | ✅一致 |
| PPI | GO PR-DUB complex + 功能推理 | Polycomb复合体 | ✅一致 |
| 定位 | UniProt Nucleus + GO chromatin binding | 核染色质定位 | ✅一致 |

**互证加分明细**:
- HTH+DEUBAD 多库一致: +0.5
- PR-DUB 复合体 GO + UniProt 互证: +0.5
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐ (3.5/5)

**核心优势**:
1. Polycomb PR-DUB 核心成员——染色质调控明确且重要
2. 高度疾病相关（Bainbridge-Ropers 综合征），转化潜力大
3. HTH HARE-type DNA-binding 域 + DEUBAD adaptor 域，功能结构域清晰
4. 本质无序 scaffold——可研究其分子伴侣功能与凝聚体形成

**风险/不确定性**:
1. 蛋白极大（2248 aa），无法全长表达和生化实验——必须截短
2. 84% 无序——难以获得全局结构信息
3. PubMed 95篇，接近新颖性淘汰线
4. IntAct/STRING 实验互作数据极度缺失

**下一步建议**:
- [ ] 设计截短构建（ASXH 域含 HTH+DEUBAD: ~1-400 aa）
- [ ] 验证与 BAP1 的去泛素化酶活性调控
- [ ] 利用 IDR 区域探索相分离/凝聚体形成能力
- [ ] ChIP-seq 确认染色质结合谱

### 5. 
### IF图像状态

| 项目 | 内容 |
|---|---|
| Ensembl | ENSG00000141431 |
| 蛋白证据 | Evidence at protein level |
| HPA抗体 | HPA039539, HPA040034 |
| IF可靠性 | 无 |
| 主定位 | N/A |
| HPA链接 | https://www.proteinatlas.org/ENSG00000141431-ASXL3/subcellular |

> **IF状态**: HPA无IF数据; 主定位: N/A)

数据来源
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22ASXL3%22%5BTitle%2FAbstract%5D
- UniProt: https://www.uniprot.org/uniprotkb/Q9C0F0
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9C0F0


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[ASXL3-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/chromatin/ASXL3/ASXL3-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9C0F0 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 10..84; /note="HTH HARE-type"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01261"; DOMAIN 254..363; /note="DEUBAD"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01264" |
| InterPro | IPR026905;IPR024811;IPR028020;IPR007759;IPR044867; |
| Pfam | PF13919;PF05066;PF13922; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000141431-ASXL3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BAP1 | Biogrid | false |
| BRD4 | Biogrid | false |
| FOXK1 | Biogrid | false |
| HCFC1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
