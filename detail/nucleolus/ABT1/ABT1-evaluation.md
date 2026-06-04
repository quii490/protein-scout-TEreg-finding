---
type: protein-evaluation
gene: "ABT1"
date: 2026-05-29
tags: [protein-scout, nuclear-protein, evaluation, ]
status: scored
---

## ABT1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | ABT1 / hABT1 (Activator of Basal Transcription 1) |
| 蛋白大小 | 272 aa / 31.1 kDa |
| UniProt ID | Q9ULW3 (ABT1_HUMAN) |
| 评估日期 | 2026-05-28 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24.0 | UniProt: Nucleus/Nucleolus; GO: Nucleus (TAS); Protein Atlas IF显示Vesicles (Approved)与功能证据矛盾 |
| 📏 蛋白大小 | 8/10 | ×1 | 8.0 | 272 aa, 31.1 kDa (200-300 aa范围) |
| 🆕 研究新颖性 | 8/10 | ×5 | 40.0 | PubMed仅29篇 (<100, 不淘汰); 真正聚焦功能研究约5篇 |
| 🏗️ 三维结构 | 7/10 | ×3 | 21.0 | 平均pLDDT=77.0; 65%残基≥70; RRM域pLDDT=87.3; 无PDB实验结构; 基线6 |
| 🧬 调控结构域 | 8/10 | ×2 | 16.0 | RRM(nucleic acid binding)多库确认; 基线7 |
| 🔗 PPI | 4/10 | ×3 | 12.0 | 调控相关10%; 主要partner为核仁/核糖体生成蛋白; IGHMBP2实验验证互作唯一亮点 |
| **加权总分** | | | **121/180**** |
| **归一化总分 (÷1.83)** | | | **66.1/100**** |  |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| GeneCards | 无法访问（Cloudflare阻断） | — |
| Protein Atlas (IF) | **Vesicles** (抗体HPA077039, Approved) | 用IF验证的唯一定位 |
| UniProt | Nucleus, Nucleolus | ECO:0000250 (by similarity to yeast Esf2) |
| GO Cellular Component | Nucleus (TAS, PMID:10648625), Nucleolus (IBA) | TAS=实验验证 |
| 原始文献 (PMID:10648625) | 核蛋白，TBP在HeLa核提取物中结合 | 实验证据 |

**关键矛盾**: Protein Atlas IF（唯一的抗体HPA077039）在Hep-G2、SK-MEL-30、U2OS三个细胞系中均显示Vesicles定位，无任何核信号。然而原始鉴定论文（PMID:10648625）明确指出ABT1是"novel mouse nuclear protein"，通过HeLa核提取物中的TBP结合和体外转录激活实验确认为核蛋白。2023年JCI Insight论文进一步证实ABT1参与核仁pre-rRNA加工。这种矛盾可能是抗体HPA077039的局限性（如交叉反应、表位遮蔽）所致。**综合判断：基于功能实验的核定位证据链完整，但IF数据构成风险**。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/ABT1/IF_images/HepG2_ABT1_1.jpg|HepG2_ABT1_1]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/ABT1/IF_images/SKMEL30_ABT1_1.jpg|SKMEL30_ABT1_1]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/ABT1/IF_images/U2OS_ABT1_1.jpg|U2OS_ABT1_1]]

**结论**: 核定位可信度中等偏高。功能实验强烈支持核/核仁定位，但Protein Atlas IF数据存在重大矛盾，需独立验证（如GFP融合蛋白定位或不同抗体）。

**IF 图像**:

#### 3.2 蛋白大小评估
**评价**: 272 aa（31.1 kDa），适合多种生化实验（Co-IP、pulldown、重组表达）。尺寸较小可能限制结构域注释的丰富度，但利于体外实验。

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed 总数 | 29 |
| 最早发表年份 | 2000 |
| 真正聚焦ABT1的研究 | ~5篇 |
| Chromatin/epigenetics 比例 | 0% (无专门研究) |

**主要研究方向**:
- **2000年**: 首次鉴定——TBP结合、基础转录激活 (PMID:10648625, Mol Cell Biol)
- **2009年**: 发现与IGHMBP2互作，参与翻译机制 (PMID:19299493, Hum Mol Genet)
- **2023年**: SMARD1疾病修饰因子——ABT1增强IGHMBP2 ATPase/解旋酶活性，参与pre-rRNA加工 (PMID:36480289, **JCI Insight**)
- **2024年**: IGHMBP2突变对ABT1关联的生化影响 (PMID:38- **2025年**: 果蝇Esf2/ABT1家族基因的功能分化 (PMID:41009135, Insects)

其余25篇大多为GWAS附带提及（牛白血病病毒、自闭症、PTSD等）或同名噬菌体（PMID:41746453），非ABT1蛋白功能研究。

**评价**: 极度新颖。在人类蛋白研究中几乎空白，chromatin/epigenetics方向完全未开发。ABT1作为TBP结合蛋白和转录共激活因子的功能提示其在转录调控中的重要性，但未被系统研究。

#### 3.4 三维结构分析
| 指标 | 数值 |
|---|---|
| AlphaFold 平均 pLDDT | 77.0 |
| PDB 实验结构 | — |
| pLDDT ≥ 90 (Very high) | 40.4% (110/272) |
| pLDDT 70–89 (Confident) | 24.6% (67/272) |
| pLDDT 50–69 (Low) | 22.4% (61/272) |
| pLDDT < 50 (Very low) | 12.5% (34/272) |
| 有序区域 (pLDDT≥70) 占比 | 65.1% |
| 可用 PDB 条目 | 无实验结构 |

**分区域 pLDDT**:

| 区域 | 残基范围 | 平均pLDDT | ≥70占比 |
|---|---|---|---|
| N端无序区 | 1-38 | 44.8 | 0% |
| RRM结构域 | 46-142 | 87.3 | 92% |
| Coiled-coil | 161-191 | 96.3 | 100% |
| C端无序区 | 198-272 | 66.9 | 39% |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/ABT1/ABT1-PAE.png]]

**PAE 数值分析**:
- PAE 矩阵尺寸: 272×272
- PAE 总体均值: 18.83 Å
- PAE <5 Å 占比: 15.8%
- PAE <10 Å 占比: 29.3%
- 残基61-200区域PAE均值<2 Å → 高度折叠核心
- RRM域与coiled-coil区域间PAE=5-10 Å → 域间空间关系预测可靠

**评价**: 结构质量中等偏上。RRM结构域和coiled-coil区域高置信度折叠，但N端(1-38)几乎完全无序，C端(198-272)有部分折叠但置信度中等。PAE图显示清晰的折叠核心，但整体PAE均值较高（18.83 Å），反映无序区域的影响。无实验PDB结构可用于交叉验证。6分的评分反映了有序/无序区域的混合状态。

#### 3.5 结构域分析
| 来源 | 结构域 | 位置 | 编号 |
|---|---|---|---|
| UniProt | RRM (RNA recognition motif) | 46-142 | — |
| InterPro | ABT1/ESF2 RNA recognition motif | 46-149 | IPR034353 |
| CDD | RRM_ABT1_like | — | cd12263 |
| InterPro | Nucleotide-binding α/β plait superfamily | 1-141 | IPR012677 |
| InterPro | RNA-binding domain superfamily | 42-133 | IPR035979 |
| InterPro (Pfam) | ABT1 C-terminal conserved domain | 216-248 | IPR060368 (PF27760) |
| InterPro (Pfam) | ESF2-like coiled-coil region | 154-195 | IPR060369 (PF27577) |
| UniProt | Disordered region | 1-38, 198-272 | — |

**染色质调控潜力分析**:
- RRM是最经典的单链核酸结合结构域，主要结合RNA但也可结合ssDNA。在ABT1中，RRM可能介导与pre-rRNA或启动子DNA的结合。
- Coiled-coil域通常介导蛋白-蛋白互作，在ABT1中可能负责与IGHMBP2或TBP的相互作用。
- C端保守域（216-248）功能未知，但在进化中高度保守，可能参与调控。
- **关键发现**: GO注释包含DNA binding (IEA)、RNA binding (HDA)、transcription coactivator activity (TAS)。但无经典的chromatin-binding结构域（bromodomain、chromodomain、PHD等）。
- 结构和功能特征一致指向：RNA结合型转录/核糖体生成调控蛋白，而非经典染色质调控因子。
- 作为极新颖蛋白（<100篇文献），现有结构域注释可能不完整。

**综合评分 7/10**: 有明确核酸结合结构域(RRM)，多个数据库一致确认，功能实验支持转录调控，但缺少经典chromatin-binding模块。

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association/direct interaction, 32 total):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---|---|---|---|---|
| PRNP | protein array (direct) | 18482256 | Prion protein | ❌ |
| ESF1 | Y2H array | 14690591 | pre-rRNA processing | 否 (核仁) |
| ESF2 | Y2H array | 29054886 | pre-rRNA processing (yeast) | 否 (核仁) |
| KRR1 | Y2H array | 29054886 | Small subunit processome | 否 (核仁) |
| UTP18 | Y2H array | 29054886 | U3 snoRNA associated | 否 (核仁) |
| NOP14 | Y2H array | 29054886 | Nucleolar protein | 否 (核仁) |
| CDCA7L | Y2H | 25416956 | Transcription factor, Myc target | ✅ 转录调控 |
| TSPYL2 | Y2H | 32296183 | Chromatin remodeling factor | ✅ 染色质调控 |
| EMD | Y2H | 32296183 | Emerin, 核膜蛋白 | ⚠️ 核架构 |
| KANK2 | Y2H | 32296183 | Cytoskeletal regulator | ❌ |
| HTT | Y2H array | 32814053 | Huntingtin | ❌ |

> IntAct 中大部分互作来自酵母蛋白 (ESF2, KRR1, UTP18 等), 反映 ABT1 在 ribosome biogenesis 中的酵母保守功能。人类蛋白中 TSPYL2 和 CDCA7L 是仅有的调控相关实验互作。

**STRING 预测互作** (combined score >0.4, top 15):

| Partner | Score | 功能类别 | 调控相关? |
|---|---|---|---|
| DDX49 | 0.998 | DEAD-box RNA解旋酶，核糖体生成 | 否(核仁) |
| RRP36 | 0.995 | rRNA加工蛋白 | 否(核仁) |
| ESF1 | 0.995 | 核仁pre-rRNA加工 | 否(核仁) |
| DDX10 | 0.992 | DEAD-box RNA解旋酶，核糖体生成 | 否(核仁) |
| BYSL | 0.991 | Bystin，核糖体生成 | 否(核仁) |
| UTP25 | 0.989 | U3 snoRNA相关蛋白 | 否(核仁) |
| KRR1 | 0.988 | 小亚基processome组分 | 否(核仁) |
| DHX15 | 0.984 | DEAH-box RNA解旋酶，剪接 | 否(剪接) |
| NOP14 | 0.983 | 核仁蛋白，rRNA加工 | 否(核仁) |
| UTP6 | 0.980 | U3 snoRNA相关蛋白 | 否(核仁) |
| UTP18 | 0.978 | U3 snoRNA相关蛋白 | 否(核仁) |
| WDR3 | 0.973 | 核仁蛋白，rRNA加工 | 否(核仁) |
| NOM1 | 0.971 | 核仁蛋白 | 否(核仁) |
| DDX18 | 0.963 | DEAD-box RNA解旋酶 | 否(核仁) |
| NGDN | 0.941 | Neuroguidin，翻译调控 | 否(翻译) |
| DHX32 | 0.905 | DEAH-box RNA解旋酶 | 否(剪接) |
| **AATF** | 0.851 | 凋亡拮抗转录因子 | **是(转录调控)** |
| DDX52 | 0.850 | DEAD-box RNA解旋酶 | 否(核仁) |
| **IGHMBP2** | 0.841 | Ig mu DNA结合蛋白2 (SMARD1致病基因) | **是(DNA结合/疾病)** |
| DDX47 | 0.821 | DEAD-box RNA解旋酶 | 否(核仁) |
| **GTF3C1** | 0.820 | 通用转录因子IIIC α亚基 | **是(转录因子)** |
| DQX1 | 0.820 | RNA依赖ATP酶 | 否 |
| 其余8个 | <0.81 | UTP23/BRIX1/UTP14A/REXO4/FTSJ3/PDCD11/PWP2/KCTD19 | 否(核仁/其他) |

**已知复合体成员** (GO Cellular Component):
- **SSU processome / 90S preribosome** (yeast, GO 推断): ABT1 的酵母同源物 Esf2 是 SSU processome 的必需组分
- 在人类中属于 pre-rRNA processing machinery, 但不属于传统染色质调控复合体

**PPI 互证分析**:
- STRING + humanPPI 共同确认: **ESF1, DDX49** (核仁蛋白)
- 文献验证 (非 IntAct physical association): **IGHMBP2** (生化验证, PMID:19299493; 直接互作+功能验证, JCI Insight 2023)
- STRING + IntAct 重叠: ESF1, DDX49, UTP18, NOP14, KRR1, UTP6 等 (全部为核仁/核糖体生成蛋白)
- 调控相关比例: ~10% (STRING), ~6% (IntAct); 极低

**评价**: ABT1 的 PPI 网络以核仁 pre-rRNA processing 为主，与染色质调控几乎无直接关联。IntAct 中 32 个实验互作进一步确认了其在 ribosome biogenesis 中的核心位置。唯一亮点是实验验证的 **IGHMBP2** 互作 (SMARD1 疾病关联) 和转录因子 **GTF3C1** 的 STRING 连接。TSPYL2 和 CDCA7L 的 IntAct 互作虽然功能类别为调控相关，但均为 Y2H 高通量。整体调控相关性极低 (~10%)。评分: **4/10**。

| 结构域功能 | GO | nucleic acid binding / DNA binding / RNA binding / transcription coactivator | ✅ 与膜注释一致 |
|---|---|---|---|
| PPI | STRING + humanPPI | 重叠2个(ESF1, DDX49)均为核仁蛋白 | 部分一致(核仁方向) |
| PPI调控 | STRING调控partner vs humanPPI | 无共同调控partner | ❌ 不一致 |
| 定位 | UniProt + GO / Protein Atlas IF | UniProt/GO: 核仁/核; IF: Vesicles | ❌ 矛盾 |

**互证加分明细**:
- 结构域≥3独立来源确认RRM（UniProt + InterPro + CDD + Pfam）: **+0.5**
- 结构域功能注释(GO:nucleic acid binding)与调控潜力一致: **+0.5**
- 定位≥2独立来源确认核定位（UniProt + GO）: **+0.5**
- 真核生物高度保守（酵母Esf2必需基因，线虫/果蝇/拟南芥同源物）: **+0.5**
- 无实验PDB结构 → 三维结构互证不加分
- PPI无共同调控neighbor → PPI互证不加分

**总分**: +2.0 / max +3

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|---|---|---|---|
| 三维结构 | AlphaFold + PDB | 见 3.4 节 | — |
| 结构域 | UniProt / InterPro / Pfam | 见 3.5 节 | — |
| PPI | STRING | 见 3.6 节 | — |
| 定位 | Protein Atlas IF / UniProt / GO | Nucleus | ✅ |

### 4. 总体评价

**推荐等级**: ★★★☆☆ (3.3/5)

**核心优势**:
1. **极度新颖**: 29篇PubMed中真正聚焦ABT1功能的不超过5篇，chromatin/epigenetics方向完全空白，具有显著的首发优势
2. **核功能明确**: 作为TBP结合蛋白和基础转录激活因子，ABT1直接参与Pol II转录调控，功能定位清晰
3. **结构域-功能一致**: RRM + coiled-coil + C端保守域的域架构支持核酸结合和蛋白互作功能，与转录共激活因子角色吻合
4. **疾病关联**: 作为SMARD1的首个疾病修饰基因(JCI Insight 2023)，ABT1具有临床转化潜力
5. **进化保守**: 从酵母到人类保守，酵母Esf2为必需基因，提示核心生物学功能重要性

**风险/不确定性**:
1. **🔴 Protein Atlas IF矛盾**: 唯一抗体(HPA077039)在三个细胞系中均显示Vesicles而非核定位。这是最重大的风险——若内源ABT1主要分布于非核区室，则核蛋白假设需重新评估。需要通过GFP-ABT1融合蛋白或独立抗体进行验证
2. **PPI以核仁/核糖体生成为主**: 可能提示ABT1的主要生理功能是rRNA加工而非Pol II转录调控，与"基础转录激活因子"的命名不完全一致
3. **无实验结构**: 完全依赖AlphaFold预测，且12.5%残基无序，N端(1-38)几乎完全无序
4. **缺少经典chromatin-binding结构域**: RRM是RNA结合域，主要与pre-rRNA互作已被2023年论文证实；ABT1与染色质/DNA的直接互作缺乏实验证据

**下一步建议**:
- [ ] **优先解决IF矛盾**: 构建GFP-ABT1进行活细胞定位，或使用不同商业抗体进行IF验证
- [ ] **ChIP-seq / CUT&RUN**: 验证ABT1在基因组上的结合位点，确认其是否直接结合启动子DNA（如原始论文推测）或通过rDNA参与核仁功能
- [ ] **ABT1 interactome**: 使用BioID/APEX2邻近标记或IP-MS鉴定核内互作组，补充STRING/humanPPI中缺失的核调控伙伴
- [ ] **SMARD1机制延展**: 利用已有的IGHMBP2-ABT1复合体知识，探索ABT1在运动神经元疾病中的核仁应激/转录调控角色
- [ ] **结构域功能验证**: 通过截短体和点突变解析RRM、coiled-coil、C端保守域的各自功能

### 5. 关键文献

1. Oda T et al. (2000). "A novel TATA-binding protein-binding protein, ABT1, activates basal transcription and has a yeast homolog that is essential for growth". *Mol Cell Biol*, 20(4):1407-18. PMID: 10648625
2. Oda T et al. (2004). "ABT1-associated protein (ABTAP), a novel nuclear protein conserved from yeast to mammals, represses transcriptional activation by ABT1". *J Cell Biochem*, 93(4):788-806. PMID: 15372600
3. de Planell-Saguer M et al. (2009). "Biochemical and genetic evidence for interaction between IGHMBP2 and ABT1". *Hum Mol Genet*, 18(11):2116-25. PMID: 19299493
4. Ricard N et al. (2023). "ABT1 serves as a disease modifier of SMARD1 by enhancing IGHMBP2 activities". *JCI Insight*, 8(3):e165381. PMID: 36480289
5. Tafforeau L et al. (2013). "The complexity of human ribosome biogenesis revealed by systematic nucleolar screening of Pre-rRNA processing factors". *Mol Cell*, 51(4):539-51. PMID: 21873635

### 6. 数据来源
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9ULW3
- UniProt: https://www.uniprot.org/uniprotkb/Q9ULW3
- InterPro: https://www.ebi.ac.uk/interpro/protein/reviewed/Q9ULW3/
- STRING: https://string-db.org/api/json/interaction_partners?identifiers=ABT1&species=9606&limit=30
- humanPPI: http://prodata.swmed.edu/humanPPI/results/Q9ULW3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000146109-ABT1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=(ABT1)
- 原始鉴定论文: https://pubmed.ncbi.nlm.nih.gov/10648625/ (Oda et al., Mol Cell Biol, 2000)
- SMARD1修饰因子论文: https://pubmed.ncbi.nlm.nih.gov/36480289/ (JCI Insight, 2023)
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=ABT1 (访问受限)


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[ABT1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。

HPA IF 图像已本地嵌入。



PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/ABT1/ABT1-PAE.png]]




