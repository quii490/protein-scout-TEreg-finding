---
type: protein-evaluation
gene: "ALKBH8"
date: 2026-05-29
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ALKBH8 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ALKBH8 / ABH8 |
| 蛋白大小 | 664 aa / ~75.2 kDa |
| UniProt ID | Q96BT7 |
| 评估日期 | 2026-05-29 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7 | ×4 | 28 | HPA IF Supported: Nucleoplasm + Microtubules; UniProt: Nucleus+Cytoplasm |
| 📏 蛋白大小 | 10 | ×1 | 10 | 664 aa，200–800 最优区间 |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed 32 篇（21–50） |
| 🏗️ 三维结构 | 8 | ×3 | 24 | AlphaFold pLDDT 80.5 + 3 PDB 实验结构 |
| 🧬 调控结构域 | 8 | ×2 | 16 | RRM 核酸结合域 + Fe2OG dioxygenase + 甲基转移酶域 |
| 🔗 PPI | 4/10 | ×3 | **12** | 详见 3.6 PPI 分析 |
| ➕ 互证加分 | +1 | max +3 | 1 | PDB + AlphaFold 结构一致，HPA + UniProt 核定位一致 |
| **原始总分** |  |  | **133/183** |  |
| **归一化总分** |  |  | **72.7/100** |  |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | — | — |
| Protein Atlas (IF) | Nucleoplasm (main); Microtubules, Mitotic spindle, Primary cilium | IF: Supported (HPA038724/HPA038725/HPA061514) |
| UniProt | Cytoplasm, Nucleus | 实验验证 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ALKBH8/IF_images/A431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ALKBH8/IF_images/U251MG_1.jpg|U-251MG]]

**结论**: HPA IF 确认 Nucleoplasm 为 main location (Supported 级别)，同时显示微管和纺锤体信号。UniProt 标注 Nucleus + Cytoplasm。核定位有 HPA IF 和 UniProt 双重确认，但胞质信号不可忽略。核定位特异性得分 7（UniProt Nucleus + HPA IF Supported，但有胞质/微管信号）。

#### 3.2 蛋白大小评估
**评价**: 664 aa，处于 200–800 aa 最优区间，适合生化实验。

#### 3.3 研究现状
| 指标 | 数值 |
|------|------|
| PubMed 总数 | 32 |
| 最早发表年份 | 2009 |
| Chromatin/epigenetics 比例 | 低（主要为 tRNA 修饰和肿瘤） |

**主要研究方向**:
- tRNA wobble uridine 修饰（主要功能）
- 结直肠癌肿瘤发生 (PMID: 41083459)
- 神经元突触形成与记忆 (PMID: 39495910)
- DNA damage response 参与

**关键文献**:
1. Madhwani KR et al. (2024). "tRNA modification enzyme-dependent redox homeostasis regulates synapse formation and memory". *Proc Natl Acad Sci U S A*. PMID: 39495910
2. Qian Y et al. (2025). "ALKBH8-mediated codon-specific translation promotes colorectal tumorigenesis". *Nat Commun*. PMID: 41083459
3. Aherrahrou R et al. (2023). "Genetic Regulation of SMC Gene Expression and Splicing Predict Causal CAD Genes". *Circ Res*. PMID: 36597873
4. Wilson JCJ et al. (2025). "WEE1 inhibitors synergise with mRNA translation defects via activation of the kinase GCN2". *Nat Commun*. PMID: 41068143
5. Madhwani KR et al. (2023). "tRNA modification enzyme-dependent redox homeostasis regulates synapse formation and memory". *bioRxiv*. PMID: 38014328

**评价**: 32 篇文献，非常新颖。研究主要集中于 tRNA 修饰功能，近期出现肿瘤（Nat Commun 2025）和神经科学（PNAS 2024）方向的高影响力论文。染色质/表观遗传方向几乎空白。

#### 3.4 三维结构分析
| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 80.5 |
| 有序区域 (pLDDT>70) 占比 | 79% |
| pLDDT > 90 占比 | 51% |
| pLDDT < 50 占比 | 14% |
| 可用 PDB 条目 | 3 (3THP: 3.20A X-ray; 3THT: 3.01A X-ray; 2CQ2: NMR) |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ALKBH8/ALKBH8-PAE.png]]

**PDB 实验结构**:
- 3THP: X-ray 3.20A, 残基 25–355 (RRM + Fe2OG 域), 2011 年
- 3THT: X-ray 3.01A, 残基 25–355, 四聚体
- 2CQ2: NMR, 残基 25–125 (RRM 域, NESG 结构基因组学)

**评价**: AlphaFold 预测质量良好（均值 80.5，79% >70）。PDB 有 3 个实验结构，覆盖 RRM + dioxygenase 域（aa 25–355, ~50% 全长），分辨率中等（3.0–3.2A）。C 端甲基转移酶域（aa 411–664）仅有预测结构，含无序区（515–575）。结构得分 8（AlphaFold 高质量 + PDB 实验验证）。

#### 3.5 结构域分析
| 来源 | 结构域 |
|------|--------|
| UniProt | RRM (43–120), Fe2OG dioxygenase (220–337), Methyltransferase domain (411–664) |
| SMART | — |
| InterPro/Pfam | IPR012677 Nucleotide-binding alpha-beta plait; IPR027450 AlkB-like; IPR025714 Methyltransferase domain |

**染色质调控潜力分析**: ALKBH8 含 RRM (RNA Recognition Motif) 核酸结合域，直接结合 tRNA。Fe2OG dioxygenase 域与 AlkB 家族的去甲基化酶活性相关。甲基转移酶域催化 tRNA 修饰。主要功能为 tRNA wobble 尿嘧啶修饰的分步催化，非染色质调控蛋白。但 RRM 域具有核酸结合能力，且参与 DNA damage response (GO IDA)。结构域得分 8（核酸结合域 RRM，多库确认，但功能为 tRNA 修饰）。

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):
| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| TRMT112 | two-hybrid/co-IP | — | tRNA 甲基转移酶辅因子 | 否 |
| FLNA | two-hybrid | — | 细胞骨架 | 否 |

**STRING 预测互作** (combined score >0.4):
| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| TRMT112 | 0.995 | tRNA 甲基转移酶辅因子 (exp=0.625) | 否 |
| ALKBH1 | 0.953 | DNA/RNA 去甲基化酶 | 是 |
| ALKBH2 | 0.835 | DNA 修复去甲基化酶 | 是 |
| ALKBH7 | 0.812 | 去甲基化酶 | 否 |
| ALKBH3 | 0.770 | RNA 去甲基化酶 | 否 |
| TRMT11 | 0.769 | tRNA 修饰酶 | 否 |
| ALKBH4 | 0.763 | 去甲基化酶 | 否 |
| ELP3 | 0.751 | 转录延伸/组蛋白乙酰转移酶 | 是 |
| FTO | 0.742 | RNA 去甲基化酶 | 是 |
| BUD23 | 0.741 | rRNA 甲基转移酶 | 否 |
| N6AMT1 | 0.728 | 甲基转移酶 | 否 |
| CTU1 | 0.702 | tRNA 修饰酶 | 否 |
| NSUN2 | 0.624 | tRNA/RNA 甲基转移酶 | 否 |

**已知复合体成员** (GO Cellular Component):
- GO:0005654 nucleoplasm (IDA:HPA)
- GO:0005634 nucleus (IDA:UniProtKB)
- 无染色质调控复合体注释

**PPI 互证分析**:
- STRING + IntAct 共同确认: TRMT112
- 仅 STRING 预测: ALKBH 家族、tRNA 修饰酶
- 仅 IntAct 实验: FLNA
- 调控相关比例: 4/14 (29%)

**评价**: PPI 网络核心为 tRNA 修饰酶通路。TRMT112 是唯一有强实验证据的互作伴侣（exp=0.625），作为 TRMT112 复合体成员共同参与 tRNA 修饰。调控相关伙伴包括 ELP3（转录延伸/组蛋白乙酰转移酶）和 ALKBH1（DNA/RNA 去甲基化酶），但均为 textmining 预测。PPI 得分 4（STRING >0.7 但以 textmining/co-expression 为主，邻居极少调控）。
##### PPI 数据源补充核查（自动审计）

**IntAct/BioGrid 实验互作核查**:
| Partner | 方法 | PMID |
|---------|------|------|
| — | cross-linking study | 30021884 |
| — | validated two hybrid | 32296183 |
| — | validated two hybrid | 32296183 |
| — | two hybrid array | 32296183 |
| — | two hybrid array | 32296183 |
| — | two hybrid prey pooling approach | 32296183 |
| — | two hybrid prey pooling approach | 32296183 |
| — | anti tag coimmunoprecipitation | 26496610 |
| — | two hybrid | 20123966 |
| — | pull down | 20123966 |

**STRING 预测/整合互作核查**:
| Partner | Score |
|---------|-------|
| TRMT112 | 0.995 |
| ALKBH1 | 0.953 |
| ALKBH2 | 0.835 |
| ALKBH7 | 0.812 |
| ALKBH3 | 0.770 |
| TRMT11 | 0.769 |
| ALKBH4 | 0.763 |
| ELP3 | 0.751 |
| FTO | 0.742 |
| BUD23 | 0.741 |

**GO-CC 复合体/定位核查**:
- GO:0005737: cytoplasm (IDA:UniProtKB)
- GO:0005829: cytosol (IDA:UniProtKB)
- GO:0005654: nucleoplasm (IDA:HPA)
- GO:0005634: nucleus (IDA:UniProtKB)

**补充结论**: PPI 评分仍以报告评分表为准；本节用于补齐 IntAct、STRING、GO-CC 三源审计证据。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT + PDB (3THP/3THT) | AF 80.5 + PDB X-ray 3.0–3.2A | 一致 |
| 结构域 | UniProt / InterPro / Pfam | RRM + Fe2OG + Methyltransferase | 一致 |
| PPI | STRING + IntAct | TRMT112 通路 | 一致 |
| 定位 | Protein Atlas IF / UniProt | Nucleoplasm (HPA) + Nucleus (UniProt) | 一致 |

**互证加分明细**:
- PDB (X-ray) + AlphaFold 结构一致: +0.5
- HPA IF (Supported) + UniProt 核定位一致: +0.5
**总分**: +1 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (3/5)

**核心优势**:
1. 新颖（32 篇），近 2 年出现高影响力论文（Nat Commun, PNAS）
2. 三域结构独特：RRM + dioxygenase + 甲基转移酶，均与核酸修饰相关
3. PDB 有实验结构（X-ray 3.0A）、AlphaFold 高质量，结构研究基础扎实

**风险/不确定性**:
1. 主要功能为胞质 tRNA 修饰，染色质/DNA 调控非主要方向
2. HPA 显示微管/纺锤体定位，非专一核蛋白
3. DNA damage response 角色待明确

**下一步建议**:
- [ ] 探究 DNA damage response 中的核功能
- [ ] 利用现有 PDB 结构进行小分子探针设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=ALKBH8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000137760
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22ALKBH8%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprotkb/Q96BT7
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96BT7
- PDB: https://www.ebi.ac.uk/pdbe/entry/pdb/3THP

![[ALKBH8-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ALKBH8/ALKBH8-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96BT7 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 43..120; /note="RRM"; DOMAIN 220..337; /note="Fe2OG dioxygenase"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00805" |
| InterPro | IPR027450;IPR015095;IPR051422;IPR034256;IPR013216;IPR012677;IPR005123;IPR035979;IPR000504;IPR029063; |
| Pfam | PF13532;PF09004;PF08241;PF00076; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000137760-ALKBH8/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| TRMT112 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
