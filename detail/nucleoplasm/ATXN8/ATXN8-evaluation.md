---
type: protein-evaluation
gene: "ATXN8"
date: 2026-06-01
tags: [protein-scout, nucleoplasm, evaluation]
status: scored
---

## ATXN8 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | ATXN8 / Ataxin-8 |
| 蛋白大小 | 80 aa / 10.3 kDa |
| UniProt ID | Q156A1 |
| 评估日期 | 2026-06-01 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | UniProt Nucleus ECO:0000269 (experimental); GO nucleus IEA |
| 蛋白大小 | 2/10 | ×1 | 2.0 | 80 aa / 10.3 kDa, 极小型蛋白 |
| 研究新颖性 | 8/10 | ×5 | 40.0 | PubMed strict=21, broad=36 |
| 三维结构 | 8/10 | ×3 | 24.0 | pLDDT 97.4; 98.8% >90; 无PDB实验结构 |
| 调控结构域 | 2/10 | ×2 | 4.0 | 无已知结构域 (InterPro/Pfam均为空) |
| PPI 网络 | 5/10 | ×3 | 15.0 | STRING 15 partners (线粒体DNA相关); IntAct 0 entries |
| **加权总分** | | | **117/180**** | |
| 互证加分 | | | +1.0 | UniProt experimental nucleus (ECO:0000269) |
| **归一化总分 (÷1.83)** | | | **63.9/100**** | |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 证据等级 |
|---|---|---|
| UniProt | Nucleus | ECO:0000269 (experimental evidence) |
| GO-CC | Nucleus | IEA:UniProtKB-SubCell (inferred from electronic annotation) |
| HPA | No IF image available | — |

**结论**: ATXN8拥有UniProt实验验证的核定位 (ECO:0000269)，这是最强的定位证据等级。作为Ataxin家族成员，其核定位与该家族参与核内RNA/转录调控的功能一致。HPA未提供IF图像。**评分: 8/10**。

**HPA IF 状态**: HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。 — HPA搜索ATXN8返回页面存在，但无IF免疫荧光图像。基因页面搜索成功但未提供亚细胞定位数据。核定位基于UniProt ECO:0000269实验证据。

#### 3.2 蛋白大小评估
80 aa / 10.3 kDa，为极小型蛋白。虽然小蛋白表达纯化简便，但可能缺乏足够的结构域复杂度用于调控功能研究。小于100 aa的蛋白在分离检测中难度增加。**评分: 2/10**。

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed strict | 21 |
| PubMed broad | 36 |
| 主要研究方向 | 脊髓小脑性共济失调8型 (SCA8)、神经退行性疾病、Parkinson病易感性 |

**关键文献**:
1. Adam MP et al. (1993). "Hereditary Ataxia Overview." *GeneReviews*. PMID: 20301317
2. Chen IC et al. (2012). "ATXN8 -62 G/A promoter polymorphism and risk of Taiwanese Parkinson's disease." *Eur J Neurol*. PMID: 22577844
3. Wu YR et al. (2009). "SCA8 repeat expansion: large CTA/CTG repeat alleles in neurological disorders and functional implications." *Hum Genet*. PMID: 19229559
4. Guo S et al. (2022). "Chinese abnormal compound heterozygote spinocerebellar ataxia type 8: a case report." *Neurol Sci*. PMID: 34993657
5. Kobayashi M (2025). "Hemichorea as the sole clinical manifestation of spinocerebellar ataxia type 8: a case report." *BMC Neurol*. PMID: 40890648

**评价**: ATXN8在SCA8研究中已有21篇文献，但由于是疾病相关基因，研究主要集中于CTG重复扩增与共济失调的遗传关联，而非其蛋白功能。该蛋白的生化功能（如核定位机制、互作网络）基本未知，从蛋白功能角度仍高度新颖。**评分: 10/10**。

#### 3.4 三维结构分析
| 指标 | 数值 |
|---|---|
| AlphaFold 平均 pLDDT | 97.4 |
| >90 | 98.8% |
| 70–90 | 1.2% |
| 50–70 | 0.0% |
| <50 | 0.0% |
| 可用 PDB 条目 | 0 (无实验结构) |

**PAE 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ATXN8/ATXN8-PAE.png]]

**评价**: pLDDT 97.4是本次9个蛋白中的最高值，98.8%残基>90表明AlphaFold对该蛋白结构预测的置信度极高。80 aa的小蛋白完全折叠，无无序区域。虽然无PDB实验结构，但AlphaFold预测质量足以支持结构分析。小型折叠良好的蛋白适合NMR结构解析。**评分: 8/10**。

#### 3.5 结构域分析
| 来源 | 结构域 |
|---|---|
| InterPro | 无记录 |
| Pfam | 无记录 |
| UniProt | 功能注释为空 |

**调控潜力**: ATXN8的InterPro和Pfam均无结构域注释，UniProt功能栏也为空。作为80 aa的极小型蛋白，其可能代表一种新型折叠或无已知同源结构的蛋白。SCA8疾病机制提示其CTG/CAG重复扩增可能通过RNA gain-of-function或polyglutamine蛋白毒性发挥作用，但其正常蛋白功能完全未知。**评分: 2/10**。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):
| Partner | Score | Experimental | Database | Textmining | 功能类别 |
|---|---|---|---|---|---|
| SSBP1 | 0.996 | 0.088 | 0 | 0.996 | mtDNA单链结合蛋白 |
| POLG | 0.996 | 0 | 0 | 0.995 | mtDNA聚合酶gamma |
| TFAM | 0.928 | 0.095 | 0 | 0.921 | mtDNA转录因子A |
| SLC25A4 | 0.921 | 0 | 0 | 0.921 | ANT1腺嘌呤核苷酸转位酶 |
| POLG2 | 0.918 | 0 | 0 | 0.915 | mtDNA聚合酶gamma辅助亚基 |
| DGUOK | 0.896 | 0 | 0 | 0.895 | 脱氧鸟苷激酶 |
| MPV17 | 0.892 | 0 | 0 | 0.892 | mtDNA维持蛋白 |
| RRM2B | 0.880 | 0 | 0 | 0.880 | p53诱导性核糖核苷酸还原酶 |
| POLRMT | 0.875 | 0 | 0 | 0.852 | mtRNA聚合酶 |
| SUCLA2 | 0.874 | 0 | 0 | 0.874 | 琥珀酰-CoA连接酶 |
| RNASEH1 | 0.869 | 0 | 0 | 0.866 | 核糖核酸酶H1 |
| MGME1 | 0.857 | 0 | 0 | 0.855 | mtDNA修复核酸外切酶 |
| DNA2 | 0.845 | 0 | 0 | 0.842 | DNA复制解旋酶/核酸酶 |
| MRPL43 | 0.806 | 0 | 0 | 0.806 | 线粒体核糖体蛋白L43 |
| GABPB1 | 0.792 | 0 | 0.750 | 0.195 | GA结合蛋白转录因子beta1 |

**IntAct 实验互作**: 0 entries found.

**UniProt 注释互作**: 无记录。

**评价**: STRING预测ATXN8的互作伙伴几乎全部为线粒体DNA代谢相关蛋白（SSBP1, POLG, POLG2, TFAM等），score极高 (≥0.99)。虽然实验证据低，但这一致性的功能富集可能暗示ATXN8在mtDNA维持或线粒体-核通讯中发挥作用。这与其主要核定位表面矛盾，可能反映双定位或条件性线粒体转运。IntAct无实验验证互作。**评分: 5/10**。

### 4. 总体评价
ATXN8是本次评估中pLDDT最高的蛋白 (97.4)，结构质量极佳。拥有实验验证的核定位 (ECO:0000269)，且PubMed文献21篇集中于SCA8疾病遗传学而非蛋白功能，因此从蛋白生化角度仍高度新颖。主要弱点是蛋白极小 (80 aa)、无已知结构域、无PDB结构、无实验验证PPI。STRONG线粒体DNA代谢蛋白的预测互作暗示可能存在未被认识的双定位或线粒体功能。适合作为一种小型折叠蛋白进行NMR结构解析和功能探索。

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ATXN8/ATXN8-PAE.png]]
