---
type: protein-evaluation
gene: "ANKRD17"
date: 2026-05-29
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ANKRD17 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ANKRD17 / GTAR, KIAA0697, MASK2, NY-BR-16 |
| 蛋白大小 | 2603 aa / ~288.9 kDa |
| UniProt ID | O75179 |
| 评估日期 | 2026-05-29 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7 | ×4 | 28 | HPA IF Supported: Nucleoplasm+核膜; GO-CC: chromatin (IDA) |
| 📏 蛋白大小 | 2 | ×1 | 2 | 2603 aa，2000–3000 区间 |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed 28 篇（21–50） |
| 🏗️ 三维结构 | 6 | ×3 | 18 | AlphaFold pLDDT 53.4, 38% >70; 新颖基线 |
| 🧬 调控结构域 | 7 | ×2 | 14 | 新颖基线；25 ANK 重复 + KH 域；chromatin binding (IDA) |
| 🔗 PPI | 6/10 | ×3 | **18** | 详见 3.6 PPI 分析 |
| ➕ 互证加分 | +1 | max +3 | 1 | HPA IF + UniProt + GO 定位一致；STRING + GO-CC 染色质证据 |
| **原始总分** |  |  | **123/183** |  |
| **归一化总分** |  |  | **67.2/100** |  |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | — | — |
| Protein Atlas (IF) | Nucleoplasm (main), Nuclear membrane (additional) | IF: Supported (HPA063731) |
| UniProt | Cytoplasm, Nucleus | 实验验证 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/ANKRD17/IF_images/CACO2_1.jpg|CACO-2]]
![[Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/ANKRD17/IF_images/U2OS_1.jpg|U2OS]]

**结论**: HPA IF (Supported) 确认 Nucleoplasm 为主要定位区室，Nuclear membrane 为附加区室。GO-CC 含 chromatin (IDA:UniProtKB)，表明染色质直接结合。GO-MF 含 chromatin binding (IDA)。UniProt 同时标注 Cytoplasm，但 HPA 仅报告核区室定位。综合判断为主要核蛋白，chromatin binding 证据强。核定位特异性得分 7（UniProt Nucleus + HPA IF + chromatin binding IDA，但胞质信号存在）。

#### 3.2 蛋白大小评估
**评价**: 2603 aa，属于超大蛋白类别（2000–3000 aa）。大量无序区占据超过一半序列，折叠域占比低。实验操作（重组表达、结晶）挑战极大。大小得分 2。

#### 3.3 研究现状
| 指标 | 数值 |
|------|------|
| PubMed 总数 | 28 |
| 最早发表年份 | 2004 |
| Chromatin/epigenetics 比例 | 中等（约 30% 涉及 DNA 复制调控和染色质互作） |

**主要研究方向**:
- 神经发育疾病（ANKRD17 相关综合征，PMID: 33909992）
- DNA 复制调控与细胞周期
- 天然免疫（抗病毒 DDX58/IFIH1 信号）
- 肝细胞癌 (PMID: 40458187)

**关键文献**:
1. Adam MP et al. (1993/2023). "ANKRD17-Related Neurodevelopmental Syndrome". *GeneReviews*. PMID: 36548456
2. Chopra M et al. (2021). "Heterozygous ANKRD17 loss-of-function variants cause a syndrome with intellectual disability, speech delay, and dysmorphism". *Am J Hum Genet*. PMID: 33909992
3. Xia D et al. (2025). "Novel ANKRD17 variants implicate synaptic and mitochondrial disruptions in intellectual disability and autism spectrum disorder". *J Neurodev Disord*. PMID: 40604385
4. Menning M et al. (2013). "A role for the Ankyrin repeat containing protein Ankrd17 in Nod1- and Nod2-mediated inflammatory responses". *FEBS Lett*. PMID: 23711367
5. Keng VW et al. (2025). "ANKRD17 induces pro-survival signaling pathways that enhance cellular invasion and migration during hepatocellular carcinoma tumorigenesis". *iScience*. PMID: 40458187

**评价**: 28 篇文献，非常新颖。主要关注点在神经发育疾病，染色质/DNA 复制调控方向仅有基础研究（PMID: 19150984），深度不足。

#### 3.4 三维结构分析
| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 53.4 |
| 有序区域 (pLDDT>70) 占比 | 38% |
| pLDDT > 90 占比 | 21% |
| pLDDT < 50 占比 | 58% |
| 可用 PDB 条目 | 0 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/ANKRD17/ANKRD17-PAE.png]]

**评价**: AlphaFold 预测质量低（均值 53.4），58% 残基 pLDDT <50。但这是预期内的——2603 aa 的大蛋白天然含有大量无序区。N 端 (1–143)、中部 (1479–1717) 和 C 端 (1906–2423) 均为 disorder 注释。ANK 重复区 (233–1414) 和 KH 域 (1725–1789) 具有较好的折叠置信度（pLDDT >70）。结构得分 6（新颖基线，符合预期）。

#### 3.5 结构域分析
| 来源 | 结构域 |
|------|--------|
| UniProt | ANK repeat ×25 (233–1414); KH domain (1725–1789) |
| InterPro/Pfam | IPR002110 Ankyrin repeat; IPR004088 KH domain |

**染色质调控潜力分析**: ANKRD17 含 25 个 ANK 重复——经典蛋白质互作模块。KH 域为 RNA 结合模块。GO-MF 含 chromatin binding (IDA:UniProtKB)，GO-BP 含 regulation of DNA replication (IMP:UniProtKB)。尽管缺乏经典 DNA 结合域，chromatin binding 活性已通过实验验证。ANK 重复可能介导染色质相关蛋白复合体组装。结构域得分 7（新颖基线，ANK+KH 域非染色质特异性，但 chromatin binding IDA 提供功能证据）。

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):
| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| 暂无高质量数据 | — | — | — | — |

**STRING 预测互作** (combined score >0.4):
| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| ANKHD1 | 0.812 | ankyrin repeat (exp=0.596) | 否 |
| HUWE1 | 0.805 | E3 泛素连接酶 | 是 (chromatin/transcription) |
| PUM1 | 0.801 | RNA binding (exp=0.272) | 否 |
| RAB3GAP1 | 0.663 | 膜运输 | 否 |
| USP34 | 0.656 | 去泛素化酶 | 否 |
| GIGYF2 | 0.639 | 翻译调控 (exp=0.262) | 否 |
| RC3H2 | 0.634 | RNA binding (exp=0.558) | 否 |
| HECTD1 | 0.604 | E3 泛素连接酶 | 是 |
| PRRC2C | 0.599 | RNA binding (exp=0.394) | 否 |
| WNK1 | 0.586 | 激酶 | 否 |
| UBAP2 | 0.576 | 泛素结合蛋白 (exp=0.352) | 否 |
| USP9X | 0.569 | 去泛素化酶 | 是 (chromatin remodeling) |
| ASXL2 | 0.563 | 染色质调控因子 (PR-DUB) | 是 |
| TRIP12 | 0.558 | E3 泛素连接酶 | 是 (DNA damage) |
| FOXK2 | 0.550 | 转录因子 | 是 |
| UBAP2L | 0.544 | RNA binding | 否 |
| SETD5 | 0.513 | 组蛋白甲基转移酶 | 是 |

**已知复合体成员** (GO Cellular Component):
- GO:0005634 nucleus (IDA:UniProtKB)
- GO:0000785 chromatin (IDA:UniProtKB)
- GO:0005654 nucleoplasm (IDA:HPA)
- GO:0031965 nuclear membrane (IDA:HPA)

**PPI 互证分析**:
- STRING + IntAct 共同确认: 无
- 仅 STRING 预测: ANKHD1 (exp=0.596), HUWE1, etc.
- 仅 IntAct 实验: 无高质量验证数据
- 调控相关比例: 6/17 (35%)

**评价**: PPI 网络包含多个染色质/转录调控因子（ASXL2、FOXK2、SETD5、HUWE1、USP9X、TRIP12）。ANKHD1 有实验证据 (exp=0.596) 但为同家族成员。ASXL2 是 PR-DUB 去泛素化酶复合体组分，直接参与染色质调控。STRING co-expression 分较高（大多数 0.5–0.8），提示共表达模式稳定。PPI 得分 6（有物理互作证据，partner 部分富集染色质调控因子 ~35%）。
##### PPI 数据源补充核查（自动审计）

**IntAct/BioGrid 实验互作核查**:
| Partner | 方法 | PMID |
|---------|------|------|
| — | two hybrid | 15102471 |
| — | tandem affinity purification | 14743216 |
| — | two hybrid | 21988832 |
| — | anti tag coimmunoprecipitation | 22190034 |
| — | pull down | 22190034 |
| — | cross-linking study | 22623428 |
| — | cross-linking study | 22623428 |
| — | anti tag coimmunoprecipitation | 19596235 |
| — | anti tag coimmunoprecipitation | 19615732 |
| — | two hybrid pooling approach | 20936779 |

**STRING 预测/整合互作核查**:
| Partner | Score |
|---------|-------|
| ANKHD1 | 0.812 |
| HUWE1 | 0.805 |
| PUM1 | 0.801 |
| RAB3GAP1 | 0.663 |
| USP34 | 0.656 |
| GIGYF2 | 0.639 |
| RC3H2 | 0.634 |
| HECTD1 | 0.604 |
| PRRC2C | 0.599 |
| WNK1 | 0.586 |

**GO-CC 复合体/定位核查**:
- GO:0000785: chromatin (IDA:UniProtKB)
- GO:0005737: cytoplasm (IDA:UniProtKB)
- GO:0016020: membrane (HDA:UniProtKB)
- GO:0031965: nuclear membrane (IDA:HPA)
- GO:0005654: nucleoplasm (IDA:HPA)
- GO:0005634: nucleus (IDA:UniProtKB)

**补充结论**: PPI 评分仍以报告评分表为准；本节用于补齐 IntAct、STRING、GO-CC 三源审计证据。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT | 53.4，ANK 域折叠，无 PDB | — |
| 结构域 | UniProt / InterPro / Pfam | ANK ×25 + KH domain | 一致 |
| PPI | STRING | ANKHD1 + chromatin regulators | 多库一致 |
| 定位 | Protein Atlas IF / UniProt / GO | Nucleoplasm (HPA) + Chromatin (GO IDA) + Nucleus (UniProt) | 一致 |

**互证加分明细**:
- HPA IF + UniProt + GO chromatin 定位三方一致: +0.5
- STRING 调控伙伴 + GO chromatin binding 功能一致: +0.5
**总分**: +1 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (3/5)

**核心优势**:
1. 实验验证的 chromatin binding（GO IDA），直接参与染色质调控
2. PPI 网络富含染色质/转录调控因子（ASXL2, FOXK2, SETD5），调控环境良好
3. 新近发现神经发育疾病基因，疾病关联性强

**风险/不确定性**:
1. 蛋白极大（2603 aa），实验操作挑战巨大
2. 主要无序，结构研究困难
3. 天然免疫和胞质功能占研究比重，核功能非主要方向
4. 功能机制研究处于早期阶段

**下一步建议**:
- [ ] 截短体设计：聚焦 ANK 重复区染色质结合片段
- [ ] ChIP-seq 鉴定基因组结合位点
- [ ] 条件性敲除细胞系用于 DNA 复制调控表型分析

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=ANKRD17
- Protein Atlas: https://www.proteinatlas.org/ENSG00000132466
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22ANKRD17%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprotkb/O75179
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75179

![[ANKRD17-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/ANKRD17/ANKRD17-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O75179 |
| SMART | SM00248;SM00322; |
| UniProt Domain [FT] | DOMAIN 1725..1789; /note="KH"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00117" |
| InterPro | IPR051631;IPR002110;IPR036770;IPR047375;IPR004087;IPR004088;IPR036612; |
| Pfam | PF00023;PF12796;PF13637;PF00013; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000132466-ANKRD17/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ANKHD1 | Biogrid, Opencell | true |
| HOXB6 | Biogrid, Opencell | true |
| BAP1 | Biogrid | false |
| CAPZB | Opencell | false |
| DDOST | Opencell | false |
| ECPAS | Biogrid | false |
| HSPA1A | Biogrid | false |
| ILF3 | Opencell | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
